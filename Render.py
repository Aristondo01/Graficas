from audioop import cross
from Obj import Obj
from random import random
from sympy import Point
from WriteUtilities import * 
from Color import *
from vector import V3
colors={'Body4': (0, 0, 1), 'Body5': (0.8, 0.8, 1), 'Body6': (0.8, 0.8, 1), 'Body11': (0.8, 0.8, 1), 'Body12': (0.8, 0.8, 1), 'Body13': (0.8, 0.8, 1), 'Body14': (0.8, 0.8, 1), 'Body15': (0.8, 0.8, 1), 'Body16': (0.8, 0.8, 1), 'Body17': (0.8, 0.8, 1), 'Body488': (0, 0, 1)}
#olors={'Body4': (0, 0, 1), 'Body5': (0.8, 0.8, 1), 'Body6': (0.8, 0.8, 1), 'Body11': (0.8, 0.8, 1), 'Body12': (0.8, 0.8, 1), 'Body13': Cara, 'Body14': (0.8, 0.8, 1), 'Body15': (0.8, 0.8, 1), 'Body16': (0.8, 0.8, 1), 'Body17': (0.8, 0.8, 1), 'Body488': (0.8, 0.8, 1)}

class Render(object):
    
    def __init__(self):
        print("Render Class Created")
        self.pointcolor(0,0,0)
        self.yVp=0
        self.xVp=0
    
    def vertexConvert (self,x,y):
        return [round(self.xVp+(x+1)*0.5*self.widthVp-1),round(self.yVp+(y+1)*0.5*self.heightVp-1)]    
    
    def viewPort (self,x,y,neww,newh):
        self.widthVp = neww
        self.heightVp = newh
        self.yVp=y
        self.xVp=x
        
    
        
    
    def backgroundcolor(self,r,g,b):
        self.color = [intcolor(r),intcolor(g),intcolor(b)]
    
    def pointcolor(self,r,g,b):
        self.pcolor =[intcolor(r),intcolor(g),intcolor(b)]
    
    def bufferStart (self, width, height):
        self.width = width
        self.height = height 
        self.heightVp =height
        self.widthVp =width
        
        self.backgroundcolor(0,0,0)
        self.clear()
        
    def clear (self):
        self.framebuffer=[
            [rgbcolor(*self.color) for x in range(self.width)]
            for y in range(self.height)
        ]
        
        self.zBuffer=[
            [-99999 for x in range(self.width)]
            for y in range(self.height)
        ]
    def write(self, filename):
        f = open(filename, 'bw')
        
        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width_bytes * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
            extra = []
            for i in range(extraBytes):
                extra.append(0)
            f.write(bytes(extra))
        f.close()
        
    def point(self, x,y):
        if not(x > self.width and x < 0 and y > self.height and x < 0):
            self.framebuffer[y][x] = rgbcolor(*self.pcolor)
    
    
    
    def bounding_box(self,A,B,C):
        xs=[A.x,B.x,C.x]
        ys=[A.y,B.y,C.y]
        
        xs.sort()
        ys.sort()
        return V3(xs[0],ys[0]),V3(xs[-1],ys[-1])
    
    def baricentric(self,A,B,C,P):
        cx,cy,cz = V3.cross(
            V3(B.x - A.x,C.x - A.x,A.x - P.x),
            V3(B.y - A.y,C.y - A.y,A.y - P.y)
        )
        
        u= cx / cz
        v= cy / cz
        w= 1 -(cx + cy)/cz 
        return (w,v,u)
        
    def triangulo(self,v1,v2,v3):

        
        L=V3(0,0,-1)
        N = (v3-v1) * (v2-v1)
        i= N.normalize() @ L.normalize()
        
        if i <= 0 or i>1:
            return
        
        self.pcolor=(round(self.pcolor[0]*i),round(self.pcolor[1]*i),round(self.pcolor[2]*i))
        
        
        
        Bmin,Bmax = self.bounding_box(v1,v2,v3)
        Bmin.round()
        Bmax.round()
        
        for x in range(Bmin.x,Bmax.x+1):
            for y in range(Bmin.y,Bmax.y+1):
                w,v,u = self.baricentric(v1,v2,v3,V3(x,y))
                
                if(w<0 or v<0 or u <0):
                    continue
                
                z= v1.z * w + v2.z * v + v3.z * u
                
                if (self.zBuffer[x][y]<z):
                    self.zBuffer[x][y]=z
                    self.point(x,y)
        pass
        
    
    def line (self,V1,V2):
        x0=V1.x
        y0=V1.y
        x1=V2.x
        y1=V2.y   
        dy = abs(y1 -y0)
        dx = abs(x1- x0)
        steep = dy > dx    
        
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        if x0>x1:
            x0,x1 = x1,x0
            y0,y1 = y1,y0
        
        dy = abs(y1 -y0)
        dx = abs(x1- x0)
        
        offset=0
        threshold = dx * 2
        y=y0
        for x in range(x0,x1+1):
            if steep:
                self.point(y,x)
                self.point(y,x+1)
                self.point(y-1,x)
                self.point(y-1,x+1)
                
                
                
                
                
            else:
                self.point(x,y)
                self.point(x+1,y)
                self.point(x,y-1)
                self.point(x+1,y-1)
                
                
                
            offset+=dy*2
            if offset >= threshold:
                y+=1 if y0<y1 else -1
                threshold+=dx*2

    def transform_vertex(self,vertex, scale, translate):
        return V3(
                round(vertex[0] * scale[0] + translate[0]),
                round(vertex[1] * scale[1] + translate[1]),
                round(vertex[2] * scale[2] + translate[2])
                
        )

    def ObjCall(self,nombre, scale_factor, translate_factor):
            figura = Obj(nombre+'.obj')
            g=None
            for face in figura.caras:
                g=face.pop()
                if(g !=None): self.pointcolor(*colors[g]) #Quitar si no hay colores
                
                if len(face)==4:
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1
                    f4 = face[3][0] - 1

                    v1 = self.transform_vertex(figura.vertices[f1], scale_factor, translate_factor)
                    v2 = self.transform_vertex(figura.vertices[f2], scale_factor, translate_factor)
                    v3 = self.transform_vertex(figura.vertices[f3], scale_factor, translate_factor)
                    v4 = self.transform_vertex(figura.vertices[f4], scale_factor, translate_factor)

                    self.triangulo(v1,v2,v3)
                    self.triangulo(v1,v3,v4)
                
                if len(face)==3:
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1

                    v1 = self.transform_vertex(figura.vertices[f1], scale_factor, translate_factor)
                    v2 = self.transform_vertex(figura.vertices[f2], scale_factor, translate_factor)
                    v3 = self.transform_vertex(figura.vertices[f3], scale_factor, translate_factor)

                    self.triangulo(v1,v2,v3)
                    
        