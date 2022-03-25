import pygame
import random
import json
import os
from Noise import Noise

class Mapc():
	def __init__(self,seed):
		self.mapdic={}
		self.bolckdic={}
		self.formation={}
		print("Mapc调用成功-version:0.1")
		self.configjson()
		self.cube=[]
		self.seed=seed
		
	def new_cube(self,pos):
		cseed=int(self.seed**2/1000000)
		sseed=int(cseed**2/1000000)
		vseed=int(sseed**2/1000000)
		p=Noise(pos[0],pos[1],cseed,sseed,vseed)
		if 
		self.cube=p
		
	
	def configjson(self):
		path0=["/storage/emulated/0/XuanWu/config/block.json","/storage/emulated/0/XuanWu/config/formation.json"]
		for p in path0:
			if not os.path.exists(p):
				print("Error:未找到json文件")
			else:
				with open(p,"r") as jsonfile:
				
					if p==path0[0]:
						self.blockdic=json.load(jsonfile)
					else:
						self.formation=json.load(jsonfile)
		return 0
		
	
		
		
	def init_mapdic(self):
		for i in range(1,101):
			self.mapdic[i]=[]
			for x in range(0,256):
				self.mapdic[i].append("grass")
		return self.mapdic
		
	def load_mapdic(self,name):
		path1="/storage/emulated/0/XuanWu/save/"+name
		if not os.path.exists(path1):
			return "Error:不存在该存档"
		else:
			with open(path1+"/mapdic.json","r") as savefile:
				
				self.mapdic=json.load(savefile)
				return self.mapdic

	def save_mapdic(self,name):
		path="/storage/emulated/0/XuanWu/save/"+name
		if not os.path.exists(path):
			os.makedirs(path)
		with open(path+"/mapdic.json","w") as savefile:
			
			jj=json.dump(self.mapdic,savefile,ensure_ascii=False)
		return 0
	def create_upper(self,name):
		dic=self.formation
		cube=[]
		bg=[]
		trylist=[]
		block=[]
		print("生成群系{}".format(name))
		for i in dic[name]["bg"]:
			bg.append(i)
		for i in range(256):
			nu=random.randint(0,len(bg)-1)
			cube.append(bg[nu])
		for item in dic[name]["block"].items():
			block.append(item[0])
		zz=0
		for i in dic[name]["block"]:
			trylist.append(block[zz])
			zz+=1
		for i in range(255):
			for t in trylist:
				p=random.randint(1,100)
				pp=100*dic[name]["block"][t]["chance"]
				if cube[i] in bg and p<=pp:
					cube[i]=t
	
		for t in trylist:
			yn=dic[name]["block"][t]["level"]
			p=100*dic[name]["block"][t]["expand"]
			yes=[]
			zancun=[]
			for x in range(yn+1):
				zz=0
			
				if zz==0:
					for i in cube:
						if i==t:
							yes.append(zz)
						zz+=1
				else:
					yes=zancun
					zancun=[]
				print(yes)
				for c in yes:
					for v in range(1,5):
						pp=random.randint(1,100)
						if pp<=p:
							if v==1 and c+16<=255:
								cube[c+16]=t
								zancun.append(c+16)
							if v==2 and c%15!=0 and c+1<=216:
								cube[c+1]=t
								zancun.append(c+1)
							if v==3 and c-16>=0:
								cube[c-16]=t
								zancun.append(c-16)
							if v==4 and c%15!=1:
								cube[c-1]=t
								zancun.append(c-1)

		self.cube=cube
		return self.cube
			
	def blit_map(self,screen):
		x=0
		y=0
		for i in self.cube:
			path="/storage/emulated/0/XuanWu/res/texture/"+i+".png"
			texture=pygame.image.load(path).convert()
			img=pygame.transform.scale(texture,(50,50))
			if x!=800:
				x+=50
			else:
				y+=50
				x=50
			screen.blit(img,(x,y))
			
	
		