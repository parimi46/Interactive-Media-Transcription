
import streamlit as st
import yt_dlp
import whisper
import os

# Load custom CSS
with open(r'D:\Gen AI\plumsoft\styles.css') as f:
    css = f.read()

# Combine both CSS styles
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Whisper model setup
model = whisper.load_model("base", device="cuda")

# Function to download audio from YouTube
def download_audio(youtube_url):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'audio_file.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return "audio_file.webm"

# Function to delete existing audio files
def delete_audio_files():
    for file in ["audio_file.webm"]:
        if os.path.exists(file):
            os.remove(file)

# Function to format time into MM:SS format
def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{int(mins):02}:{int(secs):02}"

# Function to transcribe audio using Whisper and include clickable timestamps
def transcribe_audio_with_clickable_timestamps(audio_path):
    result = model.transcribe(audio_path, verbose=True)
    transcript = [{'text': segment['text'], 'start': segment['start']} for segment in result['segments']]

    transcript_html = "<div style='color: #000; line-height: 1.8;'>"
    for segment in transcript:
        formatted_time = format_time(segment['start'])
        transcript_html += f"""
        <span style='color: #3B82F6; cursor: pointer; padding-right: 15px;' data-time='{segment['start']}'>
        [{formatted_time}]
        </span> <span style='padding-left: 10px;'>{segment['text']}</span><br>
        """
    transcript_html += "</div>"

    return transcript_html

# Streamlit app logic
st.title("Listen & Learn: Interactive Transcription of YouTube Video")

# Input for YouTube link
youtube_url = st.text_input("Enter YouTube video URL:")

# Process the input
if youtube_url:
    # Extract video ID from the URL for embedding
    video_id = youtube_url.split("v=")[-1].split("&")[0]
    embed_url = f"https://www.youtube.com/embed/{video_id}?enablejsapi=1"
    st.markdown(f'''
      <iframe id="youtube-player" width="700" height="500" src="{embed_url}" frameborder="0"></iframe>          
                ''', unsafe_allow_html=True)

    # Delete previous audio files if they exist
    delete_audio_files()

    st.write("Downloading audio...")
    audio_file_path = download_audio(youtube_url)

    if audio_file_path:
        # Display the downloaded audio file
        st.write("Downloaded audio file:")
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()

        # Display the audio player
        st.audio(audio_bytes, format='audio/webm')

        # Transcribe the audio with clickable timestamps
        st.write("Transcribing audio with clickable timestamps...")
        transcription_html = transcribe_audio_with_clickable_timestamps(audio_file_path)

        # Create your HTML content with YouTube iframe
        html_content = f"""
            {transcription_html}
        
            <script>
            function loadYouTubeIframeAPI() {{
            let tag = document.createElement('script');
            tag.src = "https://www.youtube.com/iframe_api";
            let firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
             }}

            var player;

            function onYouTubeIframeAPIReady() {{
                // Access the iframe using the parent document
                const youtubeIframe = window.parent.document.querySelector('iframe');

                if (youtubeIframe) {{
                    console.log("YouTube iframe found!");

                    // Create a new player instance
                    player = new YT.Player(youtubeIframe, {{
                        height: '500',
                        width: '900',
                        videoId: '{video_id}',  // Insert the actual video ID here
                        playerVars: {{
                            'playsinline': 1,
                            'autoplay': 0 // Set to 1 for autoplay
                
                        }},
                        events: {{
                            'onReady': onPlayerReady
                        }}
                    }});
                }} else {{
                    console.error("YouTube iframe not found.");
                }}
            }}

            function onPlayerReady(event) {{
              console.log("Player ready");
                document.querySelectorAll('span[data-time]').forEach(function(span) {{
                    span.addEventListener('click', function() {{
                        const time = parseFloat(this.getAttribute('data-time'));
                        player.seekTo(time, true); // Seek to the clicked timestamp
                        if (player.playVideo()){{
                          console.log("Video started playing at timestamp", time);
                        
                        }}
                          // Start playing the video
                    }});
                }});
            }}
            // Call the function to load the API as soon as the page is fully loaded
            document.addEventListener("DOMContentLoaded", function() {{
                loadYouTubeIframeAPI();
            }});
            </script>
        """

        # Use st.components.v1.html to render the HTML
        st.components.v1.html(html_content, height=600, scrolling=True)

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)