import os
import youtube_dl
from convert import to_mp3, to_mp4

def select_output():

    output = input("Would you like to download an MP3 or an MP4?: ")
    return output


if __name__=='__main__':

    # if ''

    video_url= input("Enter YouTube URL: ")
    video_info= youtube_dl.YoutubeDL().extract_info(url= video_url,download= False)

    filetype = select_output()

    if filetype == "MP3" or "mp3":
        to_mp3(video_info)
    elif filetype == "MP4" or "mp4":
        to_mp4(video_info)