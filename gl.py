from encodings import normalize_encoding
from Render import *
from vector import V3
global r
def glInit():
    global r
    r = Render()

def glPlano(nombre,OBJ3D,w,h):
    g = Render(w,h)
    g.plano(nombre+".bmp",OBJ3D)

def glTexture(nombre):
    r.get_Texture(nombre+".bmp")


def glIntensidadLuz(num):
    r.constantLuz=num

def glPixel(coordenada, tam):
    temp = coordenada / tam
    return (temp*2)-1
    

def glCreateWindow(width, height):
    r.bufferStart(width,height)
    
def glViewPort(x, y, width, height):
    r.viewPort(x,y,width,height)

def glClear():
    r.clear()

def glClearColor(red, g, b):
    r.backgroundcolor(red,g,b)
    
def glVertex(x, y):
    r.point(*r.vertexConvert(x,y))
     
def glColor(red, g, b):
    r.pointcolor(red,g,b)
    
def glLine(x0,y0,x1,y1):
    r.line(*r.vertexConvert(glPixel(x0,500),glPixel(y0,500)),*r.vertexConvert(glPixel(x1,500),glPixel(y1,500)))

def glLine2(x0,y0,x1,y1):
    r.line(int(x0),int(y0),int(x1),int(y1))
    
def glTriangulo (V1,V2,V3):
    r.triangulo((V1,V2,V3))

def glLoadMMatriz (translate_factor,scale_factor,rotate):
    r.loadModelMatriz(translate_factor,scale_factor,rotate)

def glCamaraVista(tipo):
    if  (tipo.lower()=="medium"):
        #r.lookAt(eye, center, up)
        r.lookAt((0,0,1), (0,0,0), (0,1,0))
    elif(tipo.lower()=="high"):
        r.lookAt((1,1,0), (0.6,0.3,0), (0,1,0.1))
    elif(tipo.lower()=="low"):
        r.lookAt((1,0,0), (0.2,0.2,0), (0,1,0.1))
    elif(tipo.lower()=="dutch"):
        r.lookAt((1,0,0), (0,0,0), (0,0.5,0.2))
        
        
        

def glRellenar(arreglo):
    tam= len(arreglo)
    maxx=0
    maxy=0
    minx=1000
    miny=1000
    coordenada=[]
    Pequeño=[]
    
    for i in range(len(arreglo)):
        if(arreglo[i][0]>maxx):
            maxx=arreglo[i][0]
        if(arreglo[i][0]<minx):
            minx=arreglo[i][0]
            
        if(arreglo[i][1]>maxy):
            maxy=arreglo[i][1]
        if(arreglo[i][1]<miny):
            miny=arreglo[i][1]
    coordenada.append(round(minx+(maxx-minx)/2))
    coordenada.append(round(miny+(maxy-miny)/2))
    r.point(coordenada[0],coordenada[1])
    
    for j in range(90):
        for i in range(len(arreglo)):
            glLine2(*arreglo[i%tam],*(arreglo[(i+1)%tam]))
            x=0
            y=0
            if(arreglo[i][0]<coordenada[0]):
                x=arreglo[i][0]+1
            elif(arreglo[i][0]>coordenada[0]):
                x=arreglo[i][0]-1
            else:
                x=arreglo[i][0]
                
                
            if(arreglo[i][1]<coordenada[1]):
                y=arreglo[i][1]+1
            elif(arreglo[i][1]>coordenada[1]):
                y=arreglo[i][1]-1
            else:
                y=arreglo[i][1]
                
                
            Pequeño.append([x,y])
        arreglo=Pequeño
        Pequeño=[]             

def glLookAt(eye, center, up):
    r.lookAt(eye, center, up)

def obj3D(nombre,color):
    r.ObjCall(nombre,color)

def glFinish(nombre):
    r.write(nombre+'.bmp') 

def glFondo(nombre):
    r.fondo(nombre+".bmp")

