class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            print(filename+" abierto")
        
        self.vertices = []
        self.caras = []
        self.tvertices=[]
        self.body=[]
        currentg=None
        
        for line in self.lines:
            if (line!="" and len(line.split(' ',1))>1):
                prefix, value =line.split(' ',1)
            if prefix == 'v':
                self.vertices.append(
                    list( 
                            map(float, value.split(' '))
                        )
                    )
            if prefix == 'vt':
                self.tvertices.append(
                    list( 
                            map(float, value.split(' '))
                        )
                    )
            
            if prefix == 'f':
                self.caras.append([
                    list(map(int,face.split('/')))
                    for face in value.split(' ')
                    ]+[currentg])
            if prefix == 'g':
                self.body.append(value)
                currentg=value