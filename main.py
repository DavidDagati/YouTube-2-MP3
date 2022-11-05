import os
import youtube_dl
from pathvalidate import sanitize_filepath
from convert import to_mp3, to_mp4

def select_output():

    output = input("Would you like to download an MP3 or an MP4?: ")
    return output

def check_directory():

    current = os.getcwd()
    search = "\\Downloaded"

    if not os.path.isdir(current + search):
        os.mkdir(current + search)

def select_filename():

    filename = input("What would you like to name your file?: ")
    clean_filename = sanitize_filepath(filename)

    return clean_filename


if __name__=='__main__':

    check_directory()

    video_url= input("Enter YouTube URL: ")
    video_info= youtube_dl.YoutubeDL().extract_info(url= video_url,download= False)

    # for i, format in enumerate(video_info['formats']):
    #    print(f"[{i}] {format['format']}")

    filetype = select_output()
    name = select_filename()

    if filetype == "MP3" or "mp3":
        filename = name + ".mp3"
        to_mp3(filename, video_info)
    elif filetype == "MP4" or "mp4":
        filename = name + "mp4"
        to_mp4(filename, video_info)