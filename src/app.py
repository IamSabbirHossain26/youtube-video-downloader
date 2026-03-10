import streamlit as st
import yt_dlp

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")

st.title("🎥 YouTube Video Downloader")
st.write("Enter a YouTube link below to get the direct download link.")

url = st.text_input("YouTube Video URL:")

if st.button("Get Download Link"):
    if url:
        ydl_opts = {'format': 'best', 'quiet': True, 'no_warnings': True}
        
        with st.spinner("Extracting link... Please wait."):
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url', None)
                    title = info.get('title', 'Video')
                    
                    if video_url:
                        st.success(f"Ready to download: **{title}**")
                        st.markdown(f"[👉 Click Here to Download Video]({video_url})", unsafe_allow_html=True)
                        st.info("Note: Right-click the link and select 'Save link as...' if it opens in the browser.")
            except Exception as e:
                st.error(f"Error extracting video: Is the link correct?")
    else:
        st.warning("Please enter a valid YouTube URL.")