import math
import random
class AI(Actor.Actor):
        
        RL = 10.0 # 도로 길이
        Loc= [0,0,1]
        I = 0
        AIcarpos = Math3d.Vector3(0,0,0)
        N = 40
        W = [[0]*8 for i in range(8)]
        W[0][0],W[1][0],W[2][0],W[3][0],W[4][0],W[5][0],W[6][0],W[7][0] = [0,0],[1,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0] # 0 = 막힘 / 1 = 뚫림
        W[0][1],W[1][1],W[2][1],W[3][1],W[4][1],W[5][1],W[6][1],W[7][1] = [0,1],[0,0],[0,1],[0,0],[0,0],[1,0],[1,0],[0,0]
        W[0][2],W[1][2],W[2][2],W[3][2],W[4][2],W[5][2],W[6][2],W[7][2] = [0,1],[1,0],[1,1],[1,0],[1,1],[0,0],[0,1],[0,0]
        W[0][3],W[1][3],W[2][3],W[3][3],W[4][3],W[5][3],W[6][3],W[7][3] = [0,1],[0,0],[0,1],[0,0],[0,0],[0,0],[0,1],[0,0]
        W[0][4],W[1][4],W[2][4],W[3][4],W[4][4],W[5][4],W[6][4],W[7][4] = [0,1],[0,0],[0,1],[1,0],[1,0],[1,0],[1,1],[0,0]
        W[0][5],W[1][5],W[2][5],W[3][5],W[4][5],W[5][5],W[6][5],W[7][5] = [0,1],[0,0],[0,1],[0,0],[0,0],[0,0],[0,1],[0,0]
        W[0][6],W[1][6],W[2][6],W[3][6],W[4][6],W[5][6],W[6][6],W[7][6] = [0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[0,0]
        W[0][7],W[1][7],W[2][7],W[3][7],W[4][7],W[5][7],W[6][7],W[7][7] = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
        speed = RL/N
        count = 0
        phase = 0
        angle = 0
        A = 0
        flag = 0 # 0:직진 1:우회전 2:좌회전
        
        
        def GetNextLoc(self,r):
              
                if(self.Loc[2] == 0):
                        if(r==0): #직진
                                self.Loc[0] = self.Loc[0] - 1

                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[0] += 1
                                    self.GetNextLoc(random.randint(1,2))               
                                else :
                                    print("직진")
                                    self.flag = 0

                        elif(r==1): # 우회전
                                self.Loc[0] = self.Loc[0] - 1
                                self.Loc[1] = self.Loc[1] + 1
                                self.Loc[2] = 3

                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[0] += 1
                                    self.Loc[1] -= 1
                                    self.Loc[2] = 0
                                    self.GetNextLoc(random.randint(0,1)*2)
                                else  :
                                    print("우회전")
                                    self.flag = 1
                        else: # 좌회전
                                self.Loc[0] = self.Loc[0] - 1
                                self.Loc[2] = 2

                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[0] += 1
                                    self.Loc[2] = 0
                                    self.GetNextLoc(random.randint(0,1))
                                else :
                                    print("좌회전")
                                    self.flag = 2

                elif(self.Loc[2] == 1):
                        if(r==0): #직진
                                self.Loc[0] = self.Loc[0] + 1

                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[0] -= 1
                                    self.GetNextLoc(random.randint(1,2))
                                else:
                                    print("직진")
                                    self.flag = 0

                        elif(r==1): # 우회전
                                self.Loc[2] = 2

                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[2] = 1
                                    self.GetNextLoc(random.randint(0,1)*2)
                                else:
                                    print("우회전")
                                    self.flag = 1

                        else: # 좌회전
                                self.Loc[1] = self.Loc[1] + 1
                                self.Loc[2] = 3

                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[1] -= 1
                                    self.Loc[2] = 1
                                    self.GetNextLoc(random.randint(0,1))
                                else :
                                    print("좌회전")
                                    self.flag = 2

                elif(self.Loc[2] == 2):
                        if(r==0): #직진
                                self.Loc[1] = self.Loc[1] - 1

                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[1] += 1
                                    self.GetNextLoc(random.randint(1,2))
                                else:
                                    print("직진")
                                    self.flag = 0
                        elif(r==1): # 우회전
                                self.Loc[1] = self.Loc[1] - 1
                                self.Loc[2] = 0

                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[1] += 1
                                    self.Loc[2] = 2
                                    self.GetNextLoc(random.randint(0,1)*2)
                                else:
                                    print("우회전")
                                    self.flag = 1

                        else: # 좌회전
                                self.Loc[0] = self.Loc[0] + 1
                                self.Loc[1] = self.Loc[1] - 1
                                self.Loc[2] = 1

                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[0] -= 1
                                    self.Loc[1] += 1
                                    self.Loc[2] = 2
                                    self.GetNextLoc(random.randint(0,1))
                                else:
                                    print("좌회전")
                                    self.flag = 2

                elif(self.Loc[2] == 3):
                        if(r==0): #직진
                                self.Loc[1] = self.Loc[1] + 1
                                if(self.W[self.Loc[0]][self.Loc[1]][1] == 0):
                                    self.Loc[1] -= 1
                                    self.GetNextLoc(random.randint(1,2))
                                else:
                                    print("직진")
                                    self.flag = 0
                        elif(r==1): # 우회전
                                self.Loc[0] = self.Loc[0] + 1
                                self.Loc[2] = 1
                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[0] -= 1
                                    self.Loc[2] = 3
                                    self.GetNextLoc(random.randint(0,1)*2)
                                else:
                                    print("우회전")
                                    self.flag = 1
                        else: # 좌회전
                                self.Loc[2] = 0
                                if(self.W[self.Loc[0]][self.Loc[1]][0] == 0):
                                    self.Loc[2] = 3
                                    self.GetNextLoc(random.randint(0,1))
                                else:   
                                    print("좌회전")
                                    self.flag = 2
                return
        def GetLoc(self):

            self.Loc[0] = int(self.AIcarpos.x)
            self.Loc[1] = int(self.AIcarpos.z)

            if (self.AIcarpos.x == self.Loc[0]):
                if((self.AIcarpos.z - self.Loc[1]) > (self.RL / 2)):
                    self.Loc[2] = 0
                    self.angle = -math.pi/2
                elif((self.AIcarpos.z - self.Loc[1]) < (self.RL / 2)):
                    self.Loc[2] = 1
                    self.angle = math.pi/2
            elif (self.AIcarpos.z == self.Loc[1]):
                if((self.AIcarpos.x - self.Loc[0]) > (self.RL / 2)):
                    self.Loc[2] = 3
                    self.angle = 0
                elif((self.AIcarpos.x - self.Loc[0]) < (self.RL / 2)):
                    self.Loc[2] = 2
                    self.angle = math.pi
            return
        def GetPos(self):
                if(self.Loc[2]==0):
                        return self.Loc[0],self.Loc[1]+(0.75*self.RL)
                elif(self.Loc[2]==1):
                        return self.Loc[0],self.Loc[1]+(0.25*self.RL)
                elif(self.Loc[2]==2):
                        return self.Loc[0]+(0.25*self.RL),self.Loc[1]
                else:
                        return self.Loc[0]+(0.75*self.RL),self.Loc[1]

        def EulerToQuaternionFloat(self,euler):

            cosx2 = math.cos(euler.x / 2.0)
            sinx2 = math.sin(euler.x / 2.0)
            siny2 = math.sin(euler.y / 2.0)
            cosy2 = math.cos(euler.y / 2.0)
            sinz2 = math.sin(euler.z / 2.0)
            cosz2 = math.cos(euler.z / 2.0)
        
            x = siny2 * cosx2 * sinz2 + cosy2 * sinx2 * cosz2
            y = siny2 * cosx2 * cosz2 - cosy2 * sinx2 * sinz2
            z = cosy2 * cosx2 * sinz2 - siny2 * sinx2 * cosz2
            w = cosy2 * cosx2 * cosz2 + siny2 * sinx2 * sinz2
        
            r = Math3d.Vector4(x, y, z, w)

            return r

        def Go(self):
            self.AIcarpos.x += math.sin(self.angle)*self.speed
            self.AIcarpos.z += math.cos(self.angle)*self.speed
            return 0

        def Turn(self,n): # n = 1 우  ,2 좌
            if (n==1):
                self.AIcartrans.Rotate(90,0,(0,1,0))
                self.angle += math.pi/2
            elif(n==2):
                self.AIcartrans.Rotate(-90,0,(0,1,0))
                self.angle -= math.pi/2
            return 0

        def __init__(self):
                self.AIcar = Container(0)
                return
        def OnCreate(self,uid):
                self.AIcartrans = self.AIcar.FindComponentByType("TransformGroup")
                self.AIcarpos = self.AIcartrans.GetPosition()
                self.GetLoc()
                self.GetNextLoc(random.randint(0,2))
                return
        def OnDestory(self):
                return
        def OnEnable(self):
                return
        def OnDisable(self):
                return
        def Update(self):


                if(self.flag == 0):
                    if(self.count < self.N):
                        self.Go()
                        self.count += 1
                    elif(self.count == self.N):
                        self.GetNextLoc(random.randint(0,2))
                        self.count = 0

                if(self.flag == 1):
                    if(self.count < (self.N)/4):
                        self.Go()
                        self.count += 1
                    elif(self.phase == 0 and self.count == (self.N)/4):
                        self.Turn(1)
                        self.count = 0
                        self.phase = 1
                    elif (self.phase == 1 and self. count == (self.N)/4):
                        self.GetNextLoc(random.randint(0,2))
                        self.count = 0
                        self.phase = 0

                if(self.flag==2):
                    if(self.count < 3*(self.N)/4):
                        self.Go()
                        self.count += 1
                    elif(self.phase == 0 and self.count == 3*(self.N)/4):
                        self.Turn(2)
                        self.count = 0
                        self.phase = 1
                    elif (self.phase == 1 and self. count == 3*(self.N)/4):
                        self.GetNextLoc(random.randint(0,2))
                        self.count = 0
                        self.phase = 0

                self.AIcartrans.SetPosition(self.AIcarpos)
                return
        def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
                return




