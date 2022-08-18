from gl import *


glInit()
glCreateWindow(2500,2500)
glClearColor(1, 1, 1)
glClear()
glColor(1,1,1)
color=(0,0,1)
glTexture('dino.bmp')
scale_factor = (22,22,15)
translate_factor = (1200, 200,0)
obj3D('dino',scale_factor,translate_factor,color)
glFinish('Dinosaurio')


#glPlano("dino.bmp",'dino',4096,4096)




