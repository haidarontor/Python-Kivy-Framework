from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ListProperty
from kivy.vector import Vector as Vec
from kivy.clock import Clock


class Ball(Widget):
    pass
    
class Ex29(Widget):
    vel1 = ListProperty([4,3])
    vel2 = ListProperty([3,4])

    def __init__(self, **kwargs):
        super(Ex29, self). __init__(**kwargs)
        self.ball1.pos = self.width/2, self.height/2
        self.ball2.pos = self.width/4, self.height/4
            
    def update1(self,dt):
        self.ball1.pos = Vec(self.vel1) + self.ball1.pos 
        if self.ball1.x<0: self.vel1[0] *= -1
        if self.ball1.x>self.width-50: self.vel1[0] *= -1
        if self.ball1.y<0: self.vel1[1] *= -1
        if self.ball1.y>self.height-50: self.vel1[1] *= -1
        
    def update2(self,dt):
        self.ball2.pos = Vec(self.vel2) + self.ball2.pos 
        if self.ball2.x<0: self.vel2[0] *= -1
        if self.ball2.x>self.width-50: self.vel2[0] *= -1
        if self.ball2.y<0: self.vel2[1] *= -1
        if self.ball2.y>self.height-50: self.vel2[1] *= -1
       
class Ex29App(App):
    def build(self):
        self.title = "Two Bouncing Balls"
        ex29 = Ex29()
        Clock.schedule_interval(ex29.update1, 1.0/60)
        Clock.schedule_interval(ex29.update2, 1.0/60)
        return ex29

if __name__=='__main__':
    Ex29App().run()