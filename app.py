import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from convert import to_mp3, to_mp4


class main_page(GridLayout):

    def __init__(self, **kwargs):

        super(main_page, self).__init__(**kwargs)
        # self.cols = 5

        # self.add_widget(Label(text='URL'))
        # self.url = TextInput(multiline=False)
        # self.add_widget(self.url)

        # self.add_widget(Label(text='Filename'))
        # self.filename = TextInput(multiline=False)
        # self.add_widget(self.filename)

        main_button = Button(text = 'Select File Extension',
                             size_hint=(0.5,0.1),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5}
                             )
 

        return main_button

        # convert_button = Button(text='Convert')
        # convert_button.bind(on_press=to_mp4)

        # self.add_widget(Label(text='Output'))
        # self.output = TextInput(multiline=False)
        # self.add_widget(self.output)


class YoutubeConverter(App):

    def build(self):
        return main_page()


if __name__ == '__main__':
    YoutubeConverter().run()