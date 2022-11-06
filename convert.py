import os
import shutil
import youtube_dl

def to_mp3(filename, video_info):
        
    options= {
                'format': 'bestaudio/best[ext=mp3]',
                'keepvideo': False,
                'outtmpl': filename,
            }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    
    current = os.getcwd()

    shutil.move(current + '\\' + filename, current + '\\Downloaded')

    print(f"{filename} Download Complete!")

def to_mp4(filename, video_info):
        
    options= {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
                'keepvideo': False,
                'outtmpl': filename,
            }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    current = os.getcwd()

    shutil.move(current + '\\' + filename, current + '\\Downloaded')

    print(f"{filename} Download Complete!")    