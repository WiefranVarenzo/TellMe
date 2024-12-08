import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import whisper
from pydub import AudioSegment
import tempfile
import os
import traceback

# Set path FFmpeg dan FFprobe untuk Pydub
AudioSegment.converter = r"C:\ffmpeg\tools\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\tools\ffmpeg\bin\ffprobe.exe"

# Konfigurasi model BERT Anda
output_dir = "./fine_tuned_model"
tokenizer = BertTokenizer.from_pretrained(output_dir)
model = BertForSequenceClassification.from_pretrained(output_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Fungsi untuk memprediksi teks baru
def predict_emotion(texts):
    encodings = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**encodings)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1).cpu()
    predictions = torch.argmax(probs, dim=1).tolist()

    # Dekode hasil prediksi ke label emosi
    emotion_mapping = {0: 'Love', 1: 'Joy', 2: 'Neutral', 3: 'Fear', 4: 'Anger', 5: 'Sad'}
    decoded_predictions = [emotion_mapping[p] for p in predictions]

    return decoded_predictions, probs

# Fungsi untuk menganalisis video dengan Whisper AI
def analyze_video_with_whisper(video_path):
    try:
        # Convert video to audio
        audio_path = video_path.replace('.mp4', '.wav')
        audio = AudioSegment.from_file(video_path)
        audio.export(audio_path, format="wav")

        # Load Whisper model
        model = whisper.load_model("medium")  # You can use "small", "medium", or "large" depending on your needs

        # Transcribe using Whisper model
        result = model.transcribe(audio_path)
        return result['text']
    except Exception as e:
        print(f"Error in analyze_video_with_whisper: {e}")
        raise

# Antarmuka Streamlit
st.title("Aplikasi Analisis Video dengan Whisper AI dan BERT")

uploaded_file = st.file_uploader("Unggah video Anda", type=["mp4"])

if uploaded_file is not None:
    temp_video_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(temp_video_path)

    if st.button("Analisis Video"):
        try:
            # Analisis video dan transkripsi
            transcript = analyze_video_with_whisper(temp_video_path)
            st.write("Transkripsi:", transcript)
            
            # Prediksi emosi
            texts = [transcript]
            predictions, probabilities = predict_emotion(texts)
            
            st.write("Prediksi Emosi:", predictions)
            st.write("Probabilitas:", probabilities)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
            # Show detailed error for debugging
            st.write("Error Details:")
            st.code(traceback.format_exc())
