from gl import *

objeto="R2-D2"
glInit()
glCreateWindow(2500,2500)
glClearColor(1, 1, 1)
glClear()
glColor(1,1,1)
color=(0,0,1)
glTexture(objeto)
translate_factor = (1350, 1000,200)
scale_factor = (550,550,550)
rotate = (0,-pi/3,0)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)
glFinish(objeto+"3D")


#glPlano(objeto,objeto,4096,4096)




