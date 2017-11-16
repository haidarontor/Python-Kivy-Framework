from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ListProperty
from kivy.vector import Vector as Vec
from kivy.clock import Clock

class Ball (Widget):
    pass
class Ex29 (Widget):
    vel1 = ListProperty([4,3])
    vel2 = ListProperty([3,4])
    def __init__(self,**kwargs):
        super(Ex29,self).__init__(**kwargs)
        self.ball1.pos = self.width/2, self.height/2
        self.ball2.pos = self.width/4 , self.height/4
        