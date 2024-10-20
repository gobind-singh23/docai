import streamlit as st
import whisper
import os


model = whisper.load_model("small")


st.title("MP3 File Uploader")

uploaded_file = st.file_uploader("Choose an MP3 file...", type="mp3")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.audio(uploaded_file, format = 'audio/mp3')

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok = True)

    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    print(file_path)
    st.write(f"File saved at: {file_path}")
    # Transcribe the audio file
    result = model.transcribe(file_path)
    transcription = result["text"]
    
    # Display the transcription
    st.write("Transcription:")
    st.write(transcription)
    
    # Provide a download link for the transcription
    st.download_button(
        label="Download Transcription",
        data=transcription,
        file_name="transcription.txt",
        mime="text/plain"
    )
