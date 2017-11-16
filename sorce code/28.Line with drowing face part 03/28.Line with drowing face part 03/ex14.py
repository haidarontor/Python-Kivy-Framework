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
        
        self.Head= ellie(400, 300, [400,300], -45, 225, 6)  
        self.Chin= ellie(400, 300, [400,300], 225, 315, 3)   
        self.Leye= ellie(60, 40, [250,450], 0, 360, 15)   
        self.Reye= ellie(60, 40, [550,450], 0, 360, 15)   
        self.Mouth= ellie(160, 30, [400,200], 0, 360, 25)   
         
        self.Nose= ellie(5, 50, [400,350], 0, 360, 25)   
        print(self.Chin)
        print (len(self.Chin))
        return Ex14()
    
if __name__ == '__main__':
    Ex14App().run() 
   
         

