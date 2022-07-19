from gl import *


glInit()
glCreateWindow(500,500)
glClearColor(1, 1, 1)
glClear()
glColor(0.9,0.1,0.1)
glViewPort(0,0,480,480)
menos =0
#Pared
for i in range (0, 130, 2):
    if i%2==0 :
        menos+=1
    glLine((50+i),(300-menos),(50+i),(220-menos))
    glLine((51+i),(300-menos),(51+i),(220-menos))

    

glColor(1,0,0)


#Chimenea arriba
glColor(1,0,0)
menos =0
for i in range (26):
    if i%2==0 :
        menos+=1 
    glLine((165+i),(410-menos),(190+i),(417-menos))  
    glLine((166+i),(410-menos),(190+i),(416-menos))  


#Techo
menos =0
for i in range (130):
    if i%2==0 :
        menos+=1 
    glLine((50+i),(300-menos),(130+i),(400-menos))
    glLine((51+i),(300-menos),(131+i),(400-menos))

#frontal
menos =0
regreso =1
glColor(0.95,0,0.1)
for i in range (160):
    if i%5==0 :
        menos+=1 
        
    if (i <= 80): 
        regreso=i+menos
        glLine((180+i),(154+menos),(180+i),(238+regreso))
    else:
        regreso+=-1
        glLine((180+i),(155+menos),(180+i),(238+regreso))

#puerta
menos =0
regreso =1
glColor(1,1,1)
for i in range (40):
    if i%5==0 :
        menos+=1   
    regreso=i+menos
    glLine((245+i),(154+menos),(245+i),(210+menos))

#chimenea
menos =0
menos2=0
glColor(0.95,0,0.1)
for i in range (30):
    if i%2==0 :menos+=1 
    if i%5==0: menos2+=1
    glLine((185+i),(373-menos),(185+i),(398+menos2))  

glColor(0.9,0.1,0.1)

menos =0
for i in range (20):
    if i%2==0 :
        menos+=1 
    glLine((165+i),(410-menos),(165+i),(383-menos))  


glFinish()



