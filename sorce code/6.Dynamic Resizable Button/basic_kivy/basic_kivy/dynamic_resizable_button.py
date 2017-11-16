from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Widgets (Widget):
    pass

class Dynamic_button(App):
    def build(self):
        return Widgets()
    
    
if __name__ == "__main__":
    
    Dynamic_button().run()