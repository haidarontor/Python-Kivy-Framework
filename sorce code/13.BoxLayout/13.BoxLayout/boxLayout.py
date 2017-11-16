from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('boxLayout.kv')

class MyBox(BoxLayout):
    pass
class HelloWorldApp(App):
    def build(self):
        return MyBox()
    
    
if __name__ == '__main__':
    HelloWorldApp().run()  