import os
import shutil
import youtube_dl
from pathvalidate import sanitize_filepath
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

url_helper = """
MDTextField:
    hint_text: "Enter URL"
    helper_text: "Youtube URL"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
    size_hint_x: None
    width: 300
"""

filename_helper = """
MDTextField:
    hint_text: "Enter a filename"
    helper_text: "Filename"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""
class YoutubeConverter(MDApp):

    def build(self):

        screen = Screen()

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
           
        self.filename = Builder.load_string(filename_helper)
        self.url = Builder.load_string(url_helper)

        self.mp3_button = MDRectangleFlatButton(text= "Convert to MP3",
                                           pos_hint= {'center_x': 0.4, 'center_y': 0.25})
        self.mp3_button.bind(on_release= to_mp3)

        self.mp4_button = MDRectangleFlatButton(text= "Convert to MP4",
                                           pos_hint= {'center_x': 0.6, 'center_y': 0.25})
        self.mp4_button.bind(on_release= to_mp4)                            

        screen.add_widget(self.url)
        screen.add_widget(self.filename)
        screen.add_widget(self.mp3_button)
        screen.add_widget(self.mp4_button)

        return screen

def check_directory():

    current = os.getcwd()
    search = "\\Downloaded"

    if not os.path.isdir(current + search):
        os.mkdir(current + search)


def to_mp3(self):

    video_url = self.parent.children[3].text
    filename = self.parent.children[2].text
    
    check_directory()

    video_info= youtube_dl.YoutubeDL().extract_info(url= video_url,download= False)

    clean_filename = sanitize_filepath(filename) + ".mp3"

    options= {
                'format': 'bestaudio/best[ext=mp3]',
                'keepvideo': False,
                'outtmpl': clean_filename,
            }

    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    except Exception as e:
        print(e)

    current = os.getcwd()

    shutil.move(current + '\\' + clean_filename, current + '\\Downloaded')

def to_mp4(self):

    video_url = self.parent.children[3].text
    filename = self.parent.children[2].text
    check_directory()

    video_info= youtube_dl.YoutubeDL().extract_info(url= video_url,download= False)

    clean_filename = sanitize_filepath(filename) + ".mp4"
        
    options= {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
                'keepvideo': False,
                'outtmpl': clean_filename,
            }

    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    except Exception as e:
        print(e)

    current = os.getcwd()

    shutil.move(current + '\\' + clean_filename, current + '\\Downloaded')

if __name__ == '__main__':
    
    YoutubeConverter().run()