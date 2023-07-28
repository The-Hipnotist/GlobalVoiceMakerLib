import yt_dlp, os, traceback, glob

def download_video(link: str):
    '''
    Download a video from YouTube using yt_dlp.
    '''
    if os.path.exists("original.wav"):
        os.remove("original.wav")
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192'
            }], 
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        for file in glob.glob("*.wav"):
            if os.path.exists(file):
                os.rename(file, "original.wav")
    except:
        print("An error has happened.")
        print(traceback.format_exc())
        exit(0)