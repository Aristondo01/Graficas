from gl import *

glInit()
glCreateWindow(740,640)
glClearColor(0, 1, 0)
glClear()
glColor(1,0,1)
color=(1,0,1)
camara="medium"

glFondo("jungla")

'''  '''
#Primer modelo
objeto="Falcon"
glLookAt((0,0,1), (0,0,0), (0,1,0))
glViewPort(200,200,115,115)
glTexture(objeto)
translate_factor = (1.3,1.4,0)
scale_factor = (0.45,0.45,0.45)
rotate = (0,-16*pi/18,0)
glIntensidadLuz(2.75)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)



#Segundo modelo
objeto="frog"
glLookAt((0,0,1), (0,0,0), (0,1,0))
glViewPort(500,0,90,90)
glTexture(objeto)
translate_factor = (0.2,-0.7,0)
scale_factor = (0.15,0.15,0.15)
rotate = (pi/2,0,0)
glIntensidadLuz(3.75)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)


#Tercer modelo
objeto="dino"
glLookAt((0,0,1), (0,0,0), (0,1,0))
glViewPort(0,0,150,150)
glTexture(objeto)
translate_factor = (0,-0.97,0)
scale_factor = (0.03,0.03,0.03)
rotate = (0,pi/5,0)
glIntensidadLuz(2)
glLoadMMatriz(translate_factor,scale_factor,rotate)
obj3D(objeto,color)


glFinish("Proyecto 3D")


#glPlano(objeto,objeto,128,128)




