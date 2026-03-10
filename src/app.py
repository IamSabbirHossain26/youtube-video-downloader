# app.py
from flask import Flask, request, jsonify, send_from_directory
import yt_dlp
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_frontend():
    """Serves the main HTML file."""
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    """Serves static files like app.js."""
    return send_from_directory('static', path)

@app.route('/api/get-link', methods=['POST'])
def get_download_link():
    """API endpoint to fetch the direct video download link."""
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"success": False, "error": "URL is required"}), 400

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        },
        'extractor_args': {'generic': {'impersonate': ['chrome']}}, 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)
            title = info.get('title', 'Unknown Video')
            
            if video_url:
                return jsonify({
                    "success": True, 
                    "title": title, 
                    "video_url": video_url
                })
            else:
                return jsonify({"success": False, "error": "Could not extract direct link."}), 400
                
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("[INFO] Server running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)