from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color , Line , Rectangle 


class Ex20(BoxLayout):
    def on_touch_down(self, touch):
     
        print("pos:{} \nspos:{}\n".format(touch.pos,touch.spos))
    def on_size(self ,*args):   
        self.px = []
        self.py =[]
        w = self.width
        h= self.height
        for r in range(1,10):
            rw = r/10.0
            self.px.extend([rw*w,0,rw*w,h])
            self.py.extend([0,rw*h,w,rw*h])
        self.canvas.clear()
        with self.canvas:
            Color (1,0,0)
            Rectangle(size= self.size)   
            Color(0,0,1)
            for i in range(9):
                Line(points = self.px[i*4:i*4+4],width=2)
                Line(points = self.py[i*4:i*4+4],width =2)
class Ex20App(App):
    def build(self):
        return Ex20()
if __name__ == '__main__':
    Ex20App().run()                   
                