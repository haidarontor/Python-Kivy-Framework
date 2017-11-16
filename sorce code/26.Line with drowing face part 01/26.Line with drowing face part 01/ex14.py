from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from  math import cos,sin,radians as rad

class Ex14(BoxLayout):
    pass

class Ex14App(App):
    def build(self):
        def ellie(a,b,orig,start_ang,stop_ang,seg):
            pts=[]
            step_ang =(stop_ang-start_ang)/seg
            for ang in range(start_ang,stop_ang+step_ang,step_ang):
                pts.extend([a*cos(rad(ang))+orig[0],
                            b*sin(rad(ang)) +orig[1]  ])
            return pts    

