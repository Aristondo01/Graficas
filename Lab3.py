from gl import *

A1=[[165, 380], [185, 360], [180, 330], [207, 345], [233, 330], [230, 360], [250, 380], [220, 385], [205, 410], [193, 383]]
A2=[[321, 335], [288, 286], [339, 251], [374, 302]]
A3=[[377, 249], [411, 197], [436, 249]]
A4= [[413, 177], [448, 159], [502, 88], [553, 53], [535, 36], [676, 37], [660, 52],
[750, 145], [761, 179], [672, 192], [659, 214], [615, 214], [632, 230], [580, 230],
[597, 215], [552, 214], [517, 144], [466, 180]]
A5=[[682, 175], [708, 120], [735, 148], [739, 170]]

glInit()
glCreateWindow(800,800)
glClearColor(0, 0, 0)
glColor(1,1,0)
glRellenar(A1)
glColor(0,0,1)
glRellenar(A2)
glColor(0,1,0)
glRellenar(A3)
glColor(1,0,0)
glRellenar(A4)
glColor(0,0,0)
glRellenar(A5)

glFinish('Rellenar')
