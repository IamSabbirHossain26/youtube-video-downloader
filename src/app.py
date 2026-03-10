import streamlit as st
import yt_dlp

st.set_page_config(page_title="Universal Video Downloader", page_icon="🌍", layout="centered")

st.markdown("""
    <style>
        /* General Body and Container Styling */
        .block-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            max-width: 700px;
            margin-top: 2rem;
        }
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Input Field Styling */
        .stTextInput > div > div > input {
            border: 1px solid #ced4da;
            border-radius: 5px;
            padding: 12px;
        }
        
        /* Primary Button (Get Link) */
        div[data-testid="column"]:nth-child(1) button {
            background-color: #0d6efd;
            color: white;
            width: 100%;
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
        div[data-testid="column"]:nth-child(1) button:hover {
            background-color: #0b5ed7;
        }
        
        /* Secondary Button (Reset) */
        div[data-testid="column"]:nth-child(2) button {
            background-color: #6c757d;
            color: white;
            width: 100%;
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
        div[data-testid="column"]:nth-child(2) button:hover {
            background-color: #5c636a;
        }
    </style>
""", unsafe_allow_html=True)

if 'video_url' not in st.session_state:
    st.session_state.video_url = ""

def clear_input():
    st.session_state.video_url = ""

st.markdown("<h1 style='text-align: center; color: #333;'>🌍 Universal Video Downloader</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c757d; margin-bottom: 20px;'>Enter a video link from almost any platform (YouTube, Facebook, Twitter, TikTok, Vimeo, etc.) to get the direct download link.</p>", unsafe_allow_html=True)

url = st.text_input("URL", placeholder="Enter Video URL here...", key="video_url", label_visibility="collapsed")

col1, col2 = st.columns([3, 1])

with col1:
    get_link_btn = st.button("Get Download Link")

with col2:
    reset_btn = st.button("Reset", on_click=clear_input)

if get_link_btn:
    if url:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            },
            'extractor_args': {'generic': {'impersonate': ['chrome']}}, 
        }
        
        with st.spinner("Extracting link... Please wait. This may take a moment."):
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url', None)
                    title = info.get('title', 'Unknown Video')
                    
                    if video_url:
                        st.success(f"**Ready:** {title}")
                        # Bootstrap styled success download button
                        st.markdown(f"""
                            <a href="{video_url}" target="_blank" style="display: block; text-align: center; background-color: #198754; color: white; padding: 12px; border-radius: 5px; text-decoration: none; font-weight: bold; margin-top: 10px;">
                                👉 Click Here to Download
                            </a>
                        """, unsafe_allow_html=True)
                        st.info("Note: Right-click the button above and select 'Save link as...' if the video opens and plays in the browser.")
                    else:
                        st.error("Could not extract a direct video link.")
                        
            except Exception as e:
                if "403" in str(e) or "anti-bot" in str(e).lower():
                    st.error("Error: The site is blocking our server with an anti-bot challenge. Free cloud IPs are often restricted.")
                else:
                    st.error(f"Error extracting video: {e}")
    else:
        st.warning("Please enter a valid URL.")