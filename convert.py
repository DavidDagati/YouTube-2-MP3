import youtube_dl

def to_mp3(filename, video_info):
        
    options= {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
            }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"{filename} Download Complete!")

def to_mp4(filename, video_info):
        
    options= {
                'format': 248,
                'keepvideo': False,
                'outtmpl': filename,
            }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"{filename} Download Complete!")    