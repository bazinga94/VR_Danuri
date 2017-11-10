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
    fric = 0.0004
    handlefric = 0.4
    grabhandle = False
    collchk = False
    colltimecnt=0
    start = False

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
        self.inkey()
        self.fricfunc()
        if(self.collchk):
            self.colliding()
        if(self.start):
            self.move()
        return
    
    def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
        
        if (msg == "KeyDown"):

            if(self.start==True):
            
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
                elif( number == 0x0D) : #"ENTER" : 시동 끄기
                    self.start = False
                    
            elif(self.start==False) :
                
                if( number == 0X0D) :  #"ENTER" : 시동 켜기
                    self.start = True

        
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
            self.speed=self.speed*-1
            self.collchk=True
        return




    def fricfunc(self):
        if(self.speed>self.fric):
            self.speed-=self.fric
        elif(self.speed<0 and self.speed+self.fric<0):
            self.speed+=self.fric
        if(self.grabhandle == False):
            if(self.WA>0):
                self.WA-=self.handlefric
            elif(self.WA<0):
                self.WA+=self.handlefric

    def inkey(self):
        self.grabhandle=False
        if (self.Wflag == 1):
            self.speed += 0.001*self.Rflag
        if (self.Sflag == 1):
            if (self.speed*self.Rflag  > 0):
                self.speed -= 0 
        if (self.Aflag == 1 ):
            self.grabhandle=True
            if(self.WA>-45):
                self.WA  -= 0.1
        if (self.Dflag == 1 ):
            self.grabhandle=True
            if(self.WA<45):
                self.WA += 0.1
        if (self.speed != 0):
            if(self.WA<0):
                self.cartrans.Rotate(-10*self.speed,0,(0,1,0))
                self.CA -= 10*self.speed
            if(self.WA>0):
                self.cartrans.Rotate(10*self.speed,0,(0,1,0))
                self.CA += 10*self.speed

    def move(self):
        self.carpos.x += self.speed*(math.sin(self.A2R(self.WA+self.CA)))
        self.carpos.z += self.speed*(math.cos(self.A2R(self.WA+self.CA)))
        self.cartrans.SetPosition(self.carpos)
        
    def colliding(self):
        self.colltimecnt+=1
        if(self.colltimecnt==4):
            self.speed *= 0.02
            self.collchk=False
            self.colltimecnt=0
