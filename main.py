from gl import *

objeto="R2-D2"
glInit()
glCreateWindow(480,480)
glViewPort(0,0,1024,1024)
glClearColor(1, 1, 1)
glClear()
glColor(1,1,1)
color=(0,0,1)
glTexture(objeto)
translate_factor = (0.3,0,-0.1)
scale_factor = (0.4,0.4,0.4)
rotate = (0,pi/5,0)
glLoadMMatriz(translate_factor,scale_factor,rotate)
#En cámara ingresar el tipo de toma que se desea ver
#Se dibujara en R2-D23D
camara="medium"
glCamaraVista(camara)
obj3D(objeto,color)
glFinish(objeto+"3D")


#glPlano(objeto,objeto,4096,4096)




