from gl import *

objeto="luna"
objeto="R2-D2"
glInit()
glCreateWindow(720,720)
glViewPort(0,0,720,720)
glClearColor(0, 0, 0)
glClear()
glColor(1,1,1)
color=(1,0,1)
glTexture(objeto)
#glFondo(objeto)
translate_factor = (0,-0.5,0)
scale_factor = (0.55,0.55,0.55)
rotate = (0,0,0)
glLoadMMatriz(translate_factor,scale_factor,rotate)
#En cámara ingresar el tipo de toma que se desea ver
#Se dibujara en R2-D23D
camara="medium"
glCamaraVista(camara)
obj3D(objeto,color)
glFinish(objeto+"3D")


#glPlano(objeto,objeto,4096,4096)




