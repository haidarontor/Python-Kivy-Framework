from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_file("box1.kv")
Builder.load_file("box2.kv")
Builder.load_file("box3.kv")

class Ex10(GridLayout):
    pass

class Ex10App(App):
    def build(self):
        self.x=150
        self.y=150
        return Ex10()
if __name__ == '__main__':
    Ex10App().run()
    
    
    