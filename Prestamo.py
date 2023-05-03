class Prestamo:
    
    def __init__(self, carnet, ISBN, fecha_prestamo):
        self.carnet = carnet
        self.ISBN = ISBN
        self.fecha_prestamo = fecha_prestamo
        
    def setCarnet(self, carnet):
        self.carnet = carnet
        
    def getCarnet(self):
        return self.carnet
        
    def setISBN(self, libro):
        self.ISBN = libro
        
    def getISBN(self):
        return self.ISBN
    
    def setFecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo
        
    def getFecha_prestamo(self):
        return self.fecha_prestamo
