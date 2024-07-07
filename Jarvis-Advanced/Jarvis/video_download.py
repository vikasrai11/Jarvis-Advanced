from pytube import YouTube 
def get_video_details_and_download(url,download=True):
    try:
        yt=YouTube(url)
        print("video title:",yt.title)
        video=yt.streams.get_highest_resolution()
        video.download()
        
    except Exception as e:
        print("error while downloading video")
    
    return None

        