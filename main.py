from gl import *


#glPlano("model.bmp")

glInit()
glCreateWindow(1500,1500)
glClearColor(1, 1, 1)
glClear()
glColor(1,1,1)
color=(1,1,1)
glTexture('model.bmp')
scale_factor = (585, 585,400)
translate_factor = (700, 700,50)
obj3D('Cara',scale_factor,translate_factor,color)
glFinish('Cara')



