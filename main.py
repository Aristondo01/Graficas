from gl import *
glInit()
glCreateWindow(1024,1024)
glClearColor(0.8, 1, 1)

glClear()
scale_factor = (24, 24,24)
translate_factor = (500, 250,250)
obj3D('Mandalorian',scale_factor,translate_factor)
"""
glColor(1,0,0)
glTriangulo(V3(10, 70),  V3(50, 160), V3(70, 80))
glColor(1,0,0)
glTriangulo(V3(180, 50), V3(150, 1),  V3(70, 180))
glColor(1,0,0)
glTriangulo(V3(180, 150), V3(120, 160), V3(130, 180))"""
glFinish('Mandalorian')




