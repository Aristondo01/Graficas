from Render import *
global r
def glInit():
    global r
    r = Render()

def glPixel(coordenada, tam):
    temp = coordenada / tam
    return (temp*2)-1
    

def glCreateWindow(width, height):
    r.bufferStart(width,height)
    
def glViewPort(x, y, width, height):
    r.viewPort(x,y,width,height)

def glClear():
    r.clear()

def glClearColor(red, g, b):
    r.backgroundcolor(red,g,b)
    
def glVertex(x, y):
    r.point(*r.vertexConvert(x,y))
     
def glColor(red, g, b):
    r.pointcolor(red,g,b)
    
def glLine(x0,y0,x1,y1):
    r.line(*r.vertexConvert(glPixel(x0,500),glPixel(y0,500)),*r.vertexConvert(glPixel(x1,500),glPixel(y1,500)))

def glFinish():
    r.write('a.bmp') 
    