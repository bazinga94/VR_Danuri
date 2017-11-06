class collision(Actor.Actor):
	def __init__(self):
		self.car=Container(0)
		self.wall=Container(0)
		return
	def OnCreate(self,uid):
		self.cartrans = self.car.FindComponentByType("TransformGroup")
		self.walltrans = self.wall.FindComponentByType("TransformGroup")
		self.carscriptcomponent = self.car.FindComponentByType("ScriptComponent")
		self.carscript = self.carscriptcomponent.GetActor()
		return
	def OnDestory(self):
		return
	def OnEnable(self):
		return
	def OnDisable(self):
		return
	def Update(self):
		box1=self.cartrans.GetSumBox()
		box2=self.walltrans.GetSumBox()
		if(box1.OBBIntersect(box2)==True):
			self.carscript.OnMessage("Coll_detect",0,Math3d.Vector4(0,0,0,0),Math3d.Vector4(0,0,0,0))
		return
	def OnMessage(self, msg, number, Vector4_lparm, Vector4_wparam):
		return


  
