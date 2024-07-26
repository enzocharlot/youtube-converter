import yt_dlp

def download_youtube_audio(url, output_format='mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Downloaded audio from {url} as {output_format}")

def download_from_file(file_path, output_format='mp3'):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        
    for url in urls:
        url = url.strip()
        if url:  # Ignorer les lignes vides
            download_youtube_audio(url, output_format)

# Exemple d'utilisation
file_path = 'url.txt'
download_from_file(file_path)
