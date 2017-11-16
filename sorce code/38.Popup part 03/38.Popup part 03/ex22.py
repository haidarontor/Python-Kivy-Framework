from __future__ import print_function , division
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty 

class SelectColorPopup(Popup):
    color = StringProperty()
    def on_color(self,*args):
        print("Color Selected:",args[1])
class SelectShapePopup(Popup):
    shape = StringProperty()
    def on_shape(self,*args):
        print("Shape Selected", args[1]) 
class EX22(BoxLayout):
    def selectColor(self,*args):
        SelectColorPopup().open()
    def selectShape(self, *args):
        SelectShapePopup().open()
        
class Ex22App(App):
    def build(self):
        self.title='Popups'
        return   EX22()
if __name__ == '__main__':
    Ex22App().run()
        
              
        
    
