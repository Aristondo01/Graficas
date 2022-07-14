from Render import *
r = Render(100,100)
def glInit():
    print("glInit")

def glCreateWindow(width, height):
    r = Render(width,height)
    
def glViewPort(x, y, width, height):
    print("glViewPort")

def glClear():
    r.clear()

def glClearColor(r, g, b):
    r=Render(0,0,0)
    r.backgroundcolor(rgbcolor(r,g,b))
    
def glVertex(x, y):
    print("glVertex")
     
def glColor(r, g, b):
    print("glColor")
    
def glFinish():
    print("glFinish")