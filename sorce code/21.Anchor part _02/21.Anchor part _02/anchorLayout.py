from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class MyAnchor (GridLayout):
    pass
class MyAnchorApp(App):
    def build(self):
        return MyAnchor()
    
if __name__ == '__main__':
    MyAnchorApp().run()    