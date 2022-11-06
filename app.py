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
        self.cols = 5

        self.add_widget(Label(text='URL'))
        self.url = TextInput(multiline=False)
        self.add_widget(self.url)

        self.add_widget(Label(text='Filename'))
        self.filename = TextInput(multiline=False)
        self.add_widget(self.filename)

        # create a dropdown with 10 buttons
        dropdown = DropDown()
                
        # Adding button in drop down list
        btn_mp3 = Button(text ='MP3', size_hint_y = None, height = 40)
        # binding the button to show the text when selected
        btn_mp3.bind(on_release = lambda btn_mp3: dropdown.select(btn_mp3.text))
        # then add the button inside the dropdown
        dropdown.add_widget(btn_mp3)

        # Adding button in drop down list
        btn_mp4 = Button(text ='MP4', size_hint_y = None, height = 40)
        # binding the button to show the text when selected
        btn_mp4.bind(on_release = lambda btn_mp4: dropdown.select(btn_mp4.text))
        # then add the button inside the dropdown
        dropdown.add_widget(btn_mp4)
        
        # create a big main button
        mainbutton = Button(text ='Extension', size_hint =(None, None), pos =(350, 300))
        
        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller
        # (here, the mainbutton instance) as the first argument of the callback
        # (here, dropdown.open.).
        mainbutton.bind(on_release = dropdown.open)
        
        # one last thing, listen for the selection in the
        # dropdown list and assign the data to the button text.
        dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
 

        convert_button = Button(text='Convert')
        convert_button.bind(on_press=to_mp4)

        self.add_widget(Label(text='Output'))
        self.output = TextInput(multiline=False)
        self.add_widget(self.output)


class MyApp(App):

    def build(self):
        return main_page()


if __name__ == '__main__':
    MyApp().run()