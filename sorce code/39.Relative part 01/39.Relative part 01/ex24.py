from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class Ex24(GridLayout):
    pass
class Ex24App(App):
    def build(self):
        return Ex24()
if __name__ == '__main__':
    Ex24App().run()
        
    