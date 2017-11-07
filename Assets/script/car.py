import math
class car(Actor.Actor):

    speed = 0.0
    Aflag = 0
    Dflag = 0
    Wflag = 0
    Sflag = 0
    Rflag = 1 # 후진 기어 키면 -1
    WA = 0.00 # Wheel Angle
    CA = 0.00 # Car Angle

    def R2A(self,R):
        return (180*R/math.pi)  # 라디안 -> 도 (PI -> 180)
    
    def A2R(self,A):
        return (A*math.pi/180)  # 도 -> 라디안 (180 -> PI)

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
            self.speed += 0.001*self.Rflag
        if (self.Sflag == 1):
            if (self.speed*self.Rflag  > 0):
                self.speed -= 0.001*self.Rflag     
        if (self.Aflag == 1 ):
            if(self.WA>-45):
                self.WA  -= 0.2
        if (self.Dflag == 1 ):
            if(self.WA<45):
                self.WA += 0.2
        if (self.speed != 0):
            if(self.WA<0):
                self.cartrans.Rotate(-10*self.speed,0,(0,1,0))
                self.CA -= 10*self.speed
            if(self.WA>0):
                self.cartrans.Rotate(10*self.speed,0,(0,1,0))
                self.CA += 10*self.speed
                
        self.carpos.x += self.speed*(math.sin(self.A2R(self.WA+self.CA)))
        self.carpos.z += self.speed*(math.cos(self.A2R(self.WA+self.CA)))
        self.cartrans.SetPosition(self.carpos)
        
        return
    
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if (msg == "KeyDown"):
            
            if( number == 0x41): #"A" : 핸들 좌로 꺾기
                self.Aflag = 1
            elif( number == 0x44): #"D" : 핸들 우로 꺾기
                self.Dflag = 1
            elif( number == 0x57): #"W" : 엑셀
                self.Wflag = 1
            elif( number == 0x53): #"S" : 브레이크
                self.Sflag = 1
            elif( number == 0x51) : #"Q" : 드라이브 기어
                self.Rflag = 1
            elif( number == 0x45) : #"E" : 후진 기어
                self.Rflag = -1
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


  
