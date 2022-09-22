import youtube_dl
# import re

def run():

    video_url= input("Enter YouTube URL: ")
    video_info= youtube_dl.YoutubeDL().extract_info(url= video_url,download= False)

    # yn = input(f"Is {video_info['title']} a Suitable Name? (Y/N): ")

    # if yn == "Y":
    #     filename = f"{video_info['title']}.mp3"
    # else:
    #     name= input("Enter your prefered filename: ")
    #     query= r"^[ .]|[/<>:\"\\|?*]+|[ .]$"
    #     illegal_char= re.findall(query, name)

    #     if len(illegal_char) == 0:
    #         return
    #     else:
    #         name= re.sub(query, "_", name)

    #     filename= name + ".mp3"

    filename = f"{video_info['title']}.mp3"
        
    options= {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
            }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"{filename} Download Complete!")

if __name__=='__main__':

    run()