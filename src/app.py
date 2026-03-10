import streamlit as st
import yt_dlp

st.set_page_config(page_title="Universal Video Downloader", page_icon="🌍")

st.title("🌍 Universal Video Downloader")
st.write("Enter a video link from almost any platform (YouTube, Facebook, Twitter, TikTok, Vimeo, etc.) to get the direct download link.")

url = st.text_input("Enter Video URL here:")

if st.button("Get Download Link"):
    if url:
        ydl_opts = {
            'format': 'best', 
            'quiet': True, 
            'no_warnings': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            }
        }
        
        with st.spinner("Extracting link... Please wait."):
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url', None)
                    title = info.get('title', 'Unknown Video')
                    
                    if video_url:
                        st.success(f"Ready to download: **{title}**")
                        st.markdown(f"### [👉 Click Here to Download Video]({video_url})", unsafe_allow_html=True)
                        st.info("Note: Right-click the link and select 'Save link as...' if it plays directly in the browser.")
                    else:
                        st.error("Could not extract a direct video link. The platform might be using a protected stream.")
                        
            except Exception as e:
                st.error(f"Error extracting video. The site might be unsupported, private, or blocking requests. Details: {e}")
    else:
        st.warning("Please enter a valid URL.")