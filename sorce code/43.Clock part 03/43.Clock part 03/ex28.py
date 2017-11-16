from __future__ import division
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock

class Ex28(GridLayout):
    counter1 = NumericProperty(0)
    counter2 = NumericProperty(0)
    counter3 = NumericProperty(0)
    counter4 = NumericProperty(0)
   
    def update1(self,dt): self.counter1 +=1
    def update2(self,dt): self.counter2 +=1
    def update3(self,dt): self.counter3 +=1
    def update4(self,dt): self.counter4 +=1
class Ex28App(App):
    def build(self):
        ex28 = Ex28() 
        
        Clock.schedule_interval(ex28.update1,1)   
        Clock.schedule_interval(ex28.update2,1/2)
        Clock.schedule_interval(ex28.update3,1/3) 
        Clock.schedule_interval(ex28.update4,1/4)  
        
        return ex28
if __name__ == '__main__':
    Ex28App().run()  
    