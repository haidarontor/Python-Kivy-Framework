import kivy.uix.gridlayout as TheGrid
from kivy.app import App

class MyGrid(TheGrid.GridLayout):
    pass
class MyGridApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyGridApp().run()
    