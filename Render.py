from Obj import Obj
from random import random
from sympy import Point
from WriteUtilities import * 
from Color import *
colors={'Body4': (1, 1, 1), 'Body5': (0, 0, 1), 'Body6': (0, 0, 1), 'Body11': (0, 0, 1), 'Body12': (0, 0, 1), 'Body13': (0, 0, 1), 'Body14': (0, 0, 1), 'Body15': (0, 0, 1), 'Body16': (0, 0, 1), 'Body17': (0, 0, 1), 'Body488': (1, 1, 1)}
#olors={'Body4': (1, 1, 1), 'Body5': (0, 0, 1), 'Body6': (0, 0, 1), 'Body11': (0, 0, 1), 'Body12': (0, 0, 1), 'Body13': Cara, 'Body14': (0, 0, 1), 'Body15': (0, 0, 1), 'Body16': (0, 0, 1), 'Body17': (0, 0, 1), 'Body488': (0, 0, 1)}

class Render(object):
    
    def __init__(self):
        print("Render Class Created")
        self.pointcolor(0,0,0)
        self.yVp=0
        self.xVp=0
        
    
    def vertexConvert (self,x,y):
        return [int(self.xVp+(x+1)*0.5*self.widthVp-1),int(self.yVp+(y+1)*0.5*self.heightVp-1)]    
    
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
    
    
    
    def line (self,x0,y0,x1,y1):
                
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
                #self.point(y,x-1)
                
                
                
            else:
                self.point(x,y)
                #self.point(x-1,y)
                
            offset+=dy*2
            if offset >= threshold:
                y+=1 if y0<y1 else -1
                threshold+=dx*2

    def transform_vertex(self,vertex, scale, translate):
        return [
                int(vertex[0] * scale[0] + translate[0]),
                int(vertex[1] * scale[1] + translate[1])
        ]  

    def ObjCall(self,nombre, scale_factor, translate_factor):
            figura = Obj(nombre+'.obj')
            g=None
            for face in figura.caras:
                g=face.pop()
                #colors[g]=(round(random(),2),round(random(),2),round(random(),2))
                if(g !=None): self.pointcolor(*colors[g]) #Quitar si no hay colores
                for i in range(len(face)):
                    f1 = face[i][0] - 1
                    f2 = face[(i+1)%len(face)][0] - 1

                    v1 = self.transform_vertex(figura.vertices[f1], scale_factor, translate_factor)
                    v2 = self.transform_vertex(figura.vertices[f2], scale_factor, translate_factor)

                    self.line(v1[0], v1[1], v2[0], v2[1])
            #print(colors)

        