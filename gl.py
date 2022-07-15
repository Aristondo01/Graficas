from Render import *
global r
def glInit():
    global r
    r = Render()
    

def glCreateWindow(width, height):
    r.bufferStart(width,height)
    
def glViewPort(x, y, width, height):
    print("glViewPort")

def glClear():
    r.clear()

def glClearColor(red, g, b):
    r.backgroundcolor(red,g,b)
    
def glVertex(x, y):
    print("glVertex")
     
def glColor(r, g, b):
    print("glColor")
    
def glFinish():
    r.write('a.bmp') 
    