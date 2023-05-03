import os
from datetime import datetime, timedelta

class ControllerPrestamo:
    
    def __init__(self, vista, base_datos):
        self.view = vista
        self.Model = base_datos
        
    def EjecutarPrograma(self):
        while True:
            os.system('cls')
            self.view.MostrarMenu()
            
            opcion = self.view.SolicitarDato("Ingrese una opción: ")
            os.system('cls')
            
            if opcion == "1":
                resultados = self.BusquedaFiltros()
                self.MostrarLibros(resultados)
                self.view.Questionario()
                opcion_questionario = self.view.SolicitarDato("Ingrese una opción: ")
                if opcion_questionario == "1":
                    self.SolicitarLibro()
                else:
                    os.system('cls')
            elif opcion == "2":
                self.view.MostrarDisponibles("")
            else:
                break
        
    def BusquedaFiltros(self):
        self.view.MenuBusqueda()
        opcion_busqueda = self.view.SolicitarDato("Ingrese una opción: ")
        os.system('cls')
        if opcion_busqueda == "1":
            titulo = self.view.SolicitarDato("Ingrese el título del libro: ")
            return self.Model.FiltrarLibro(2, titulo)
        elif opcion_busqueda == "2":
            autor = self.view.SolicitarDato("Ingrese el autor del libro: ")
            return self.Model.FiltrarLibro(3, autor)
        elif opcion_busqueda == "3":
            return self.Model.FiltrarLibro(5, 'none')
        return ""
    
    def MostrarLibros(self, resultados): 
        if len(resultados) == "":
            self.view.Mensaje("El libro no ha sido encontrado")
        else:
            self.view.MostrarDisponibles(resultados)

    def SolicitarLibro(self):
        isbn = self.view.SeleccionLibro()
        if self.Model.FiltrarLibro(1, isbn) == "":
            self.view.Mensaje("El libro no se encuentra disponible")
            return 
        else:
            result = self.Model.buscar_prestamos_por_ISBN(isbn)
            if len(result) != 0:
                self.view.Mensaje("El libro se encuentra prestado, estará disponible despues del " + str(result[0].getFecha_prestamo())[0:10])
                return 
            
        carnet = self.view.SolicitarCarnet()
        if self.Model.buscar_estudiante_por_carnet(carnet) == False:
            self.view.Mensaje("El estudiante no se encuentra registrado")
            return
        self.RegistrarPrestamo(isbn, carnet)
        return 

    def RegistrarPrestamo(self, ISBN, carnet):
        try:
            fecha_prestamo = datetime.now() + timedelta(days=5)
            
            self.Model.RegistrarPrestamo(ISBN, carnet, fecha_prestamo)
            self.view.Mensaje("El libro se ha prestado con éxito")
        except:
            self.view.Mensaje("El libro no se ha prestado")
