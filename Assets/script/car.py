import math
class car(Actor.Actor):

    speed = 0.0
    Aflag = 0
    Dflag = 0
    Wflag = 0
    Sflag = 0
    A = 0.00
    B = 0.00    

    def __init__(self):
        self.car=Container(0)
        return
    def OnCreate(self,uid):
        self.cartrans = self.car.FindComponentByType("TransformGroup")
        self.carpos = self.cartrans.GetPosition()
        self.carrot = self.cartrans.GetRotation()
        return
    def OnDestory(self):
        return
    def OnEnable(self):
        return
    def OnDisable(self):
        return
    def Update(self):
        
        if (self.Wflag == 1):
            self.speed += 0.001
        if (self.Sflag == 1):
            self.speed -= 0.001     
        if (self.Aflag == 1 ):
            self.cartrans.Rotate(-1,0,(0,1,0))
            self.B  -= 1
        if (self.Dflag == 1 ):
            self.cartrans.Rotate(1,0,(0,1,0))
            self.B += 1       
        self.carpos.x += self.speed*(math.cos((math.pi / 2) - (math.pi*(self.B/180))))
        self.carpos.z += self.speed*(math.sin((math.pi / 2) - (math.pi*(self.B/180))))
        self.cartrans.SetPosition(self.carpos)
        
        return
    
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if (msg == "KeyDown"):
            
            if( number == 0x41): #"A"
                self.Aflag = 1
            elif( number == 0x44): #"D"
                self.Dflag = 1
            elif( number == 0x57): #"W"
                self.Wflag = 1
            elif( number == 0x53): #"S"
                self.Sflag = 1
            
        if (msg == "KeyUp"):
            
            if( number == 0x41): #"A"
                self.Aflag = 0
            elif( number == 0x44): #"D"
                self.Dflag = 0
            elif( number == 0x57): #"W"
                self.Wflag = 0
            elif( number == 0x53): #"S"
                self.Sflag = 0
                
        if(msg == "Coll_detect"):
            print("coll")
            speed=speed*-0.1
            
                
            
        return


  
