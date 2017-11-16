from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen

from kivy.uix.widget import Widget
from kivy.graphics import Line
from screen_manager_for_multiple_screen import presenstation

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"]= Line(points=(touch.x , touch.y))
            
    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x , touch.y]    

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass 

presenstation = Builder.load_file("mainNavigation.kv")

class MainApp(App):
    def build(self):
        return presenstation
 
if __name__ == "__main__":
    MainApp().run()    