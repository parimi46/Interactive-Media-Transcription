# 🌟 Project Overview

This project is a web application designed to transcribe audio from YouTube videos and generate interactive, clickable timestamps. By leveraging cutting-edge technologies like OpenAI's Whisper model and yt-dlp, the app simplifies the process of extracting, processing, and navigating through spoken content from YouTube. Built using Streamlit, it offers a sleek and user-friendly interface for effortless interaction.

---

## ✨ Features

- 🎥 **YouTube Audio Downloading**: Extracts audio directly from YouTube videos using the `yt-dlp` library.
- 🗣️ **Speech-to-Text Transcription**: Converts audio to text using the Whisper model with high accuracy, even for diverse accents.
- 🕒 **Interactive Timestamps**: Generates clickable timestamps linked to video moments for easy navigation.
- 💻 **User-Friendly Interface**: Built with Streamlit and styled with custom CSS for a visually appealing and intuitive design.

---

## 🛠️ Technologies Used

- **Backend**: 🐍 Python
- **Frontend**: 🎨 Streamlit, Custom CSS
- **Libraries**:
  - 🔗 `yt-dlp` for audio extraction.
  - 🧠 Whisper for transcription.
  - 🗂️ `os` for file handling.

---

## 🚀 Project Workflow

1. 🔗 **Input YouTube Video URL**: Enter the YouTube video URL into the app.
2. 📥 **Audio Extraction**: `yt-dlp` downloads the audio in the best format.
3. 📝 **Transcription**: The Whisper model processes the audio and generates text with timestamps.
4. 🎯 **Interactive Output**: Text and clickable timestamps are displayed alongside the video.

---

## 🛡️ How to Use

1. **Clone this repository**:
   ```bash
   git clone https://github.com/parimi46/Interactive-Media-Transcription.git

2. **Navigate to the project folder**:
   ```bash
   cd Interactive-Media-Transcription
3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the application**:
   ```bash
   streamlit run chatbot.py

5. Open the app in your browser 🌐 and paste the YouTube video URL to start transcribing.

---

## 🎯 Key Benefits

- 🦻 **Improves accessibility** for those with hearing impairments or language barriers.
- 📚 **Helps students, researchers, and content creators** quickly reference specific parts of a video.
- ✍️ **Facilitates note-taking, content review, and multimedia learning**.

---
