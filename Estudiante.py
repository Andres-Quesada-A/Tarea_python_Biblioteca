class Estudiante:
    
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre
        
    def setCarnet(self, carnet):
        self.carnet = carnet
        
    def getCarnet(self):
        return self.carnet
