from gl import *

"""r = Render(100, 100)

r.line(50,50,0,0)
r.line(50,0,0,50)

r.write('a.bmp') """


glInit()
glCreateWindow(100,100)
glClearColor(1, 0, 0)
glClear()
glColor(1,1,1)
glViewPort(-1,-1,50,50)
glVertex(0,0)
glFinish()



