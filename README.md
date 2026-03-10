# 🌍 Universal Video Downloader

A lightweight, web-based video downloader built with Python and Streamlit. This tool allows users to extract direct download links for videos from popular platforms like YouTube, Facebook, Twitter, TikTok, and Vimeo using the powerful `yt-dlp` library.

🔗 **Live Demo:** [Try the App Here](https://all-videos-downloader.streamlit.app/)

## 🚀 Features
* **Universal Support:** Extracts direct `.mp4` download links from most standard social media and video hosting platforms.
* **Anti-Bot Bypass:** Integrated with browser impersonation capabilities (`curl_cffi`, `pycryptodomex`) to handle basic Cloudflare or 403 Forbidden errors.
* **Clean UI:** A minimal, responsive, Bootstrap-inspired user interface built directly within Streamlit.
* **No Server Storage:** Fetches the direct URL instead of downloading the video to the server, saving bandwidth and preventing server crashes.

## ⚠️ Limitations
* **Protected Content:** Cannot download DRM-protected videos or content from private/closed groups.
* **Streaming Sites:** Does not support complex movie or anime streaming sites (e.g., FileMoon, DoodStream, m3u8 HLS streams) that use heavy JavaScript obfuscation and iframe embedding. For those, browser extensions or network-tab extraction are recommended.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Frontend/Framework:** Streamlit
* **Core Engine:** yt-dlp
