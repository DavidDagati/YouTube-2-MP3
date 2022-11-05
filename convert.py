import youtube_dl


def to_mp3(video_info):

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

def to_mp4(video_info):

    filename = f"{video_info['title']}.mp4"
        
    options= {
                'format': 'bestvideo[ext=mp4]',
                'keepvideo': False,
                'outtmpl': filename,
            }



    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    

    print(f"{filename} Download Complete!")    