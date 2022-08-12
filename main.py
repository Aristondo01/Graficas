from gl import *


#glPlano("model.bmp")

glInit()
glCreateWindow(1024,1024)
glClearColor(0, 0, 0)
glClear()
glColor(1,1,1)
color=(1,1,1)

scale_factor = (455, 455,400)
translate_factor = (500, 500,50)
obj3D('Cara',scale_factor,translate_factor,color)
glFinish('Cara')



