from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

from convert import to_mp3, to_mp4


url_helper = """
MDTextField:
    hint_text: "Enter URL"
    helper_text: "Youtube URL"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    size_hint_x: None
    width: 300
"""

filename_helper = """
MDTextField:
    hint_text: "Enter a filename"
    helper_text: "Filename"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint_x: None
    width: 300
"""
class YoutubeConverter(MDApp):

    def build(self):

        screen = Screen()
        self.theme_cls.primary_palette = "Red"

        format_button = MDRectangleFlatButton(text= "Select Format",
                                       pos_hint= {'center_x': 0.5, 'center_y': 0.4},
                                       on_release= self.format_dropdown.open(self))

        convert_button = MDRectangleFlatButton(text= "Convert",
                                       pos_hint= {'center_x': 0.5, 'center_y': 0.2},
                                       on_release= self.converter)
        self.filename = Builder.load_string(filename_helper)
        self.url = Builder.load_string(url_helper)


        screen.add_widget(self.url)
        screen.add_widget(self.filename)
        screen.add_widget(format_button)
        screen.add_widget(convert_button)

        return screen

    def on_start(self):
        format_dropdown = ObjectProperty()

        self.format_dropdown = MDDropdownMenu(width_mult=3)

        self.format_dropdown.items.append(
                            {"viewclass": "MDMenuItem",
                            "text": "MP3",
                            "callback": self.format_callback},
                            {"viewclass": "MDMenuItem",
                            "text": "MP4",
                            "callback": self.format_callback}
                        )

    def option_callback(self, selected_option):
        self.selected_option = selected_option

    def converter(self, obj):
        dialog = MDDialog(title= "URL", 
                          text= self.url.text,
                          size_hint=(0.5, 1))
        dialog.open()

    def change_format(self, value):
        self.format = value

if __name__ == '__main__':
    YoutubeConverter().run()