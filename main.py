from gl import *

objeto="Falcon"
glInit()
glCreateWindow(640,640)
glClearColor(0, 1, 0)
glClear()
glColor(1,0,1)
color=(1,0,1)
camara="medium"

glFondo("jungla")


#Primer modelo
glLookAt((0,0,1), (0,0,0), (0,1,0))
glViewPort(200,200,115,115)
glTexture(objeto)
translate_factor = (1.3,1.4,0)
scale_factor = (0.5,0.5,0.5)
rotate = (0,-16*pi/18,0)
glIntensidadLuz(2.75)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)



#Segundo modelo
glLookAt((0,0,1), (0,0,0), (0,1,0))
glViewPort(0,0,115,115)
glTexture(objeto)
translate_factor = (1.3,1.4,0)
scale_factor = (0.5,0.5,0.5)
rotate = (0,-16*pi/18,0)
glIntensidadLuz(1.75)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)


glFinish("Proyecto 3D")


#glPlano(objeto,objeto,128,128)




