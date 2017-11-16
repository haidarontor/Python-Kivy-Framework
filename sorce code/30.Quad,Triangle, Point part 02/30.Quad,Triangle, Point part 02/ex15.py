from kivy.uix.boxlayout import BoxLayout
from kivy.app import App 

class Ex15(BoxLayout):
    pass
class Ex15App(App):
    def build(self):
        return Ex15()

if __name__ =='__main__':
    Ex15App().run()