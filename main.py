from gl import *
glInit()
glCreateWindow(1000,1000)
glClearColor(0, 0, 0)
glClear()
scale_factor = (22, 22)
translate_factor = (500, 250)
obj3D('Mandalorian',scale_factor,translate_factor)
glFinish('Mandalorian')




