from sympy import Point
from WriteUtilities import * 
from Color import *
class Render(object):
    
    def backgroundcolor(self,colorarray):
        self.color = intcolor(colorarray)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        #if self.width % 4 != 0: self.width+=self.width % 4
        #if self.height % 4 != 0: self.height+=self.height % 4
        self.backgroundcolor([0,0,0])
        self.clear(self.color)

    def clear (self,colors):
        self.framebuffer=[
            [rgbcolor(*colors) for x in range(self.width)]
            for y in range(self.height)
        ]
    def write(self, filename):
        f = open(filename, 'bw')
        
        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes
        
        # 1025 * 3 + 1 -> 3076
        
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
        f.write(dword(24))
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
        self.framebuffer[x][y] = rgbcolor(250,0,0)
        
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
        for x in range(x0,x1):
            offset+=dy*2
            if offset >= threshold:
                y+=1 if y0<y1 else -1
                threshold+=dx*2
                
            if steep:
                self.point(y,x)
            else:
                self.point(x,y)

        