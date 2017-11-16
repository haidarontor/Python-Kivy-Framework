from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class relativeLayout(RelativeLayout):
    pass

class relativeLayoutApp(App):
    def build(self):
        return relativeLayout()
if __name__ == '__main__':
    relativeLayoutApp().run()
    