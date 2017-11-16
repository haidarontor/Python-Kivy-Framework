from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.app import App

Builder.load_file("backgroundColor.kv")
class MyStack(StackLayout):
    pass
   
class Ex7App(App):
    def build(self):
        return MyStack()

if __name__=='__main__':
    Ex7App().run()