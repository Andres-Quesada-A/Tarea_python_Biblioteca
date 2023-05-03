from Prestamo import Prestamo

class Model:
    
    def __init__(self):
        self.Libros = []
        self.CategoriasLibros = []
        self.Prestamos = []
        self.Estudiantes = []
        
    # Métodos para el atributo Libros
    def setLibros(self, libros):
        self.Libros = libros
        
    def getLibros(self):
        return self.Libros
    
    def agregarLibro(self, libro):
        self.Libros.append(libro)
        
    def eliminarLibro(self, libro):
        self.Libros.remove(libro)
    
    # Métodos para el atributo CategoriasLibros
    def setCategoriasLibros(self, categorias):
        self.CategoriasLibros = categorias
        
    def getCategoriasLibros(self):
        return self.CategoriasLibros
    
    def agregarCategoria(self, categoria):
        self.CategoriasLibros.append(categoria)
        
    def eliminarCategoria(self, categoria):
        self.CategoriasLibros.remove(categoria)
    
    # Métodos para el atributo Prestamos
    def setPrestamos(self, prestamos):
        self.Prestamos = prestamos
        
    def getPrestamos(self):
        return self.Prestamos
    
    def RegistrarPrestamo(self, ISBN, carnet, fecha_prestamo):
        prestamo = Prestamo(carnet, ISBN, fecha_prestamo)
        self.Prestamos.append(prestamo)

        for libro in self.Libros:
            if libro.getISBN() == ISBN:
                libro.setDisponibilidad(False)
                break
        
        
    def eliminarPrestamo(self, prestamo):
        self.Prestamos.remove(prestamo)
    
    # Métodos para el atributo Estudiantes
    def setEstudiantes(self, estudiantes):
        self.Estudiantes = estudiantes
        
    def getEstudiantes(self):
        return self.Estudiantes
    
    def agregarEstudiante(self, estudiante):
        self.Estudiantes.append(estudiante)
        
    def eliminarEstudiante(self, estudiante):
        self.Estudiantes.remove(estudiante)

    def FiltrarLibro(self, opcion, filtro):
        if opcion == 1:
            # Filtrar por ISBN
            libros_filtrados = [libro for libro in self.Libros if libro.getISBN() == int(filtro)]
        elif opcion == 2:
            # Filtrar por título
            libros_filtrados = [libro for libro in self.Libros if filtro.lower() in libro.getTitulo().lower()]
        elif opcion == 3:
            # Filtrar por autor
            libros_filtrados = [libro for libro in self.Libros if filtro.lower() in libro.getAutor().lower()]
        elif opcion == 4:
            # Filtrar por categoría
            libros_filtrados = [libro for libro in self.Libros if filtro.lower() in libro.getCategoria().lower()]
        else:
            # Opción inválida
            libros_filtrados = self.Libros
            
        return self.PintarLibros(libros_filtrados)
    
    def PintarLibros(self, libros_filtrados):
        Libros_str = ""
        for libro in libros_filtrados:
            Libros_str +=libro.pintar_libro() + '\n'
        return Libros_str
    
    def buscar_estudiante_por_carnet(self, carnet):
        for estudiante in self.Estudiantes:
            if int(estudiante.getCarnet()) == int(carnet):
                return True
        return False

    def buscar_prestamos_por_ISBN(self, ISBN):
        prestamos_filtrados = [prestamo for prestamo in self.Prestamos if prestamo.getISBN() == ISBN]
        return prestamos_filtrados
