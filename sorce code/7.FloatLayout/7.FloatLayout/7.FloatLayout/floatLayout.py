from kivy.app import App

from kivy.uix.floatlayout import FloatLayout

class float_layout(App):
    def build(self):
        return FloatLayout()
    
    
if __name__ == "__main__":
    float_layout().run()