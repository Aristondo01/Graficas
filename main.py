from gl import *

objeto="R2-D2"
glInit()
glCreateWindow(2500,2500)
glClearColor(1, 1, 1)
glClear()
glColor(1,1,1)
color=(0,0,1)
glTexture(objeto)
scale_factor = (550,550,550)
translate_factor = (1300, 900,0)
obj3D(objeto,scale_factor,translate_factor,color)
glFinish(objeto+"3D")


#glPlano(objeto,objeto,4096,4096)




