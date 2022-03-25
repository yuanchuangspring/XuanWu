import numpy as np

class Noise():
 def __init__(self,x,y,cseed,sseed,vseed):
 	self.cube=[]
 	self.pos=0
 	xc=x//16
 	yc=y//16
 	c=0
 	s=0
 	v=0
 	self.s=0
 	self.c=0
 	for y in range(1,17):
 		for x in range(1,17):
 			xx=xc+x%16*0.0625
 			yy=yc+y%16*0.0625
 			v=int(self.perlin(xx,yy,vseed)*16)
 			self.cube[0].append(v)
 	s=abs(int(self.perlin(xc+xc*0.125,yc*yc+yc*0.625,sseed)*26))
 	c=abs(int(self.perlin(xc+xc*0.125,yc*yc+yc*0.625,cseed)*26))
 	self.s=s
 	self.c=c
 	if c<=2:
 		if s==0:
 			self.cube.append("redaiyulin")
 		if s>=1 and s<=2:
 			self.cube.append("redaicaoyuan")
 		if s>=3:
 			self.cube.append("redaishamo")
 	if c>=3 and c<=4:
 		if s<=2:
 			self.cube.append("wendaiyulin")
 		if s==3:
 			self.cube.append("wendaijifeng")
 		if s>=3:
 			self.cube.append("wendaicaoyuan")
 	if c>=5:
 		if s<=1:
 			self.cube.append("handaisenlin")
 		if s>=2 and s<=3:
 			self.cube.append("wendaicaoyuan")
 		if s>=4:
 			self.cube.append("taiyuan")
 	
 def perlin(self,x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = int(x)
    yi = int(y)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = self.fade(xf)
    v = self.fade(yf)
    # noise components
    n00 = self.gradient(p[p[xi]+yi],xf,yf)
    n01 = self.gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = self.gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = self.gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = self.lerp(n00,n10,u)
    x2 = self.lerp(n01,n11,u) # FIX1: I was using n10 instead of n01
    return self.lerp(x1,x2,v) # FIX2: I also had to reverse x1 and x2 here

 def lerp(self,a,b,x):
    "linear interpolation"
    return a + x * (b-a)

 def fade(self,t):
    "6t^5 - 15t^4 + 10t^3"
    return 6*t**5 - 15*t**4 + 10*t**3

 def gradient(self,h,x,y):
    "grad converts h to the right gradient vector and return the dot product with (x,y)"
    vectors = [[0,1],[0,-1],[1,0],[-1,0]]
    g = vectors[h%4]
    return g[0] * x + g[1] * y
    
