class ViewPrestamo:

    
    def MostrarMenu(self):
        print("Bienvenido a la biblioteca")
        print("1. Pedir un libro")
        print("2. Devolver un libro")
        print("0. Salir")

    
    def MenuBusqueda(self):
        print("Busqueda de un libro")
        print("1. Buscar por título")
        print("2. Buscar por autor")
        print("0. Regresar")

    def Questionario(self):
        print("Busqueda de un libro")
        print("1. Solicitar libro")
        print("0. Regresar")
        
    
    def FiltrarLibros(self):
        # Aquí iría el código para filtrar los libros
        pass
        
    
    def MostrarDisponibles(self, libros_disponibles):
        print(libros_disponibles)
    
    
    def SolicitarTitulo(self):
        titulo = input("Ingrese el título del libro: ")
        return titulo
        
    
    def SolicitarAutor(self):
        autor = input("Ingrese el autor del libro: ")
        return autor
        
    
    def SolicitarCarnet(self):
        while True:
            try:
                carnet = int(input("Ingrese su número de carnet: "))
                return carnet
            except ValueError:
                print("El carnet debe ser un valor entero. Por favor intente de nuevo.")
        
    
    def SeleccionLibro(self):
        while True:
            try:
                isbn = input("Ingrese su ISBN del libro: ")
                return isbn
            except ValueError:
                print("El ISBN debe ser un valor entero. Por favor intente de nuevo.")
        

    def Mensaje(self, mensaje):
        print(mensaje)
