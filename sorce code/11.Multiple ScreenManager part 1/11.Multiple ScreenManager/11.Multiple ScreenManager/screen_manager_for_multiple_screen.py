from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition

class MainScreen (Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presenstation=Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return  presenstation
    
MainApp().run() 
    