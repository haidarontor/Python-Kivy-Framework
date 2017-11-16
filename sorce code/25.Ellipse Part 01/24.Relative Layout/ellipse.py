from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class Ellipse(GridLayout):
    pass
class EllipseApp(App):
    def build(self):
        return Ellipse()
if __name__ == '__main__':
    EllipseApp().run()    