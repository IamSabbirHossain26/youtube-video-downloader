import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")

st.title("🎥 YouTube Video Downloader")
st.write("Enter a YouTube link below to download the video directly.")

url = st.text_input("YouTube Video URL:")

TEMP_FILENAME = "temp_video.mp4"

if st.button("Fetch Video"):
    if url:
        ydl_opts = {
            'format': 'best',
            'outtmpl': TEMP_FILENAME,
            'quiet': True,
            'no_warnings': True,
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