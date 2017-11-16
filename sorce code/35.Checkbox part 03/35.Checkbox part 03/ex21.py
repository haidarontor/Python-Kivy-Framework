from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import StringProperty


class Ex21(GridLayout):
    status =StringProperty("I am inactive")
    status1= StringProperty("I am the inactive member of the group")
    status2 = StringProperty("I am the inactive member of the group")
    def checkActive(self,*args):
        if args[1]==True:self.status="I am active"
        else:self.status = "I am inactive"
    def checkActive1(self,*args):
        if args[1]==True : self.status1 ="I am the active memeber of the group"
        else:self.status1="i am inactive member of the group"    
    def checkActive2(self,a,b):
        if b==True :self.status2="I am active member of the group"
        else: self.status2="i am the inactive member of the group "
    def checkActive3(self,*args):
        if args[1]==False :self.ids['pythonLang'].active=True
class Ex21App(App): 
    def build(self):
        self.title="CheckBoxes"
        return Ex21()
if __name__ =='__main__':
    Ex21App().run()   
    
    
           
                
