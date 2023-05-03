class Libro:
    
    def __init__(self, ISBN, titulo, autor, edicion, disponibilidad):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.disponibilidad = disponibilidad
        
    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad
        
    def getDisponibilidad(self):
        return self.disponibilidad
        
    def setISBN(self, ISBN):
        self.ISBN = ISBN
        
    def getISBN(self):
        return self.ISBN
    
    def setTitulo(self, titulo):
        self.titulo = titulo
        
    def getTitulo(self):
        return self.titulo
        
    def setAutor(self, autor):
        self.autor = autor
        
    def getAutor(self):
        return self.autor
        
    def setEdicion(self, edicion):
        self.edicion = edicion
        
    def getEdicion(self):
        return self.edicion

    def pintar_libro(self):
        String = ""
        String += "ISBN:" + str(self.ISBN) + '\n'
        String += "Título:"+ str(self.titulo) + '\n'
        String += "Autor:"+ str(self.autor) + '\n'
        String += "Edición:"+ str(self.edicion) + '\n'
        String += "Disponibilidad:" + str(self.disponibilidad) + '\n'
        return String