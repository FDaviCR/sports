from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Config.set('graphics', 'resizable', True)  
Config.set('graphics', 'borderless', False)
Config.set('graphics', 'fullscreen', 'fake')

class MyApp(App):
    def build(self):
        Window.maximize()
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Test", )
        layout.add_widget(button)
        
        return layout

    def close_app(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    MyApp().run()
