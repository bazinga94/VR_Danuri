import math
class car(Actor.Actor):

    speed = 0.01
    A = 0.00
    B = 0.00
    PI = 3.141592
    

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
        self.carpos.x += self.speed*(math.cos((math.pi / 2) - (math.pi*(self.B/180))))
        self.carpos.z += self.speed*(math.sin((math.pi / 2) - (math.pi*(self.B/180))))
        self.cartrans.SetPosition(self.carpos)
        if (self.A!=self.B):
            if (self.A < self. B):
                self.B -= 1
                self.cartrans.Rotate(-1,0,(0,1,0))
            else :
                self.B += 1
                self.cartrans.Rotate(1,0,(0,1,0))
            
            
        
        return
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        if (msg == "KeyUp"):
            if( number == 0x41): #"A"
                self.A -= 30
            elif( number == 0x44): #"D"
                self.A += 30
                self.cartrans.Rotate(30,0,(0,1,0))
            elif( number == 0x57): #"W"
                self.speed += 0.01
            elif( number == 0x53): #"S"
                self.speed -= 0.01
		if(msg == "Coll_dtect"):
			self.speed=0
            
                
            
        return


  
