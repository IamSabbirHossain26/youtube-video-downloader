import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")

st.title("🎥 YouTube Video Downloader")
st.write("Enter a YouTube link below to download the video directly.")

url = st.text_input("YouTube Video URL:")

TEMP_FILENAME = "temp_video.mp4"

if st.button("Download Video"):
    if url:
        ydl_opts = {
            'format': 'best',
            'outtmpl': TEMP_FILENAME,
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }
        }
        
        with st.spinner("Processing your video... Please wait."):
            try:
                if os.path.exists(TEMP_FILENAME):
                    os.remove(TEMP_FILENAME)
                    
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    title = info.get('title', 'Video')
                
                st.success(f"Ready: **{title}**")
                
                with open(TEMP_FILENAME, "rb") as file:
                    st.download_button(
                        label="⬇️ Download Video Now",
                        data=file,
                        file_name=f"{title}.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Error processing video. Make sure the link is correct. Details: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")