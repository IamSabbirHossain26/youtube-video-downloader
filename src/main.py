import yt_dlp
import os

def download_video(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    ydl_opts = {
        'format': 'best', 
        'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
        'quiet': False,
        'no_warnings': True,
    }

    try:
        print(f"\n[INFO] Starting download for: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[SUCCESS] Download completed successfully! Check the 'downloads' folder.")
        
    except yt_dlp.utils.DownloadError as e:
        print(f"\n[ERROR] Failed to download video. Details: {e}")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("=== YouTube Video Downloader ===")
    video_url = input("Enter the YouTube video URL: ").strip()
    
    if video_url:
        download_video(video_url)
    else:
        print("[WARNING] Invalid URL. Please run the script and try again.")