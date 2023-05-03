import os
from datetime import datetime, timedelta

class ControllerPrestamo:
    
    def __init__(self, vista, base_datos):
        self.view = vista
        self.BaseDatos = base_datos
        
    def EjecutarPrograma(self):
        while True:
            os.system('cls')
            self.view.MostrarMenu()
            
            opcion = input("Ingrese una opción: ")
            os.system('cls')
            
            if opcion == "1":
                resultados = self.BusquedaFiltros()
                self.MostrarLibros(resultados)
                self.view.Questionario()
                opcion_questionario = input("Ingrese una opción: ")
                if opcion_questionario == "1":
                    self.SolicitarLibro()
                else:
                    os.system('cls')
            elif opcion == "2":
                self.view.MostrarDisponibles()
            else:
                break
        
    def BusquedaFiltros(self):
        self.view.MenuBusqueda()
        opcion_busqueda = input("Ingrese una opción: ")
        os.system('cls')
        if opcion_busqueda == "1":
            titulo = input("Ingrese el título del libro: ")
            return self.BaseDatos.FiltrarLibro(2, titulo)
        elif opcion_busqueda == "2":
            autor = input("Ingrese el autor del libro: ")
            return self.BaseDatos.FiltrarLibro(3, autor)
        elif opcion_busqueda == "3":
            return self.BaseDatos.FiltrarLibro(5, 'none')
        return ""
    
    def MostrarLibros(self, resultados): 
        if len(resultados) == "":
            self.view.Mensaje("El libro no ha sido encontrado")
        else:
            self.view.MostrarDisponibles(resultados)

    def SolicitarLibro(self):
        isbn = self.view.SeleccionLibro()
        if self.BaseDatos.FiltrarLibro(1, isbn) == "":
            self.view.Mensaje("El libro no se encuentra disponible")
            return 
        else:
            result = self.BaseDatos.buscar_prestamos_por_ISBN(isbn)
            if len(result) != 0:
                self.view.Mensaje("El libro se encuentra prestado, estará disponible despues del " + str(result[0].getFecha_prestamo())[0:10])
                input('Presione cualquier tecla para aceptar')
                return 
            
        carnet = self.view.SolicitarCarnet()
        if self.BaseDatos.buscar_estudiante_por_carnet(carnet) == False:
            self.view.Mensaje("El estudiante no se encuentra registrado")
            input('Presione cualquier tecla para aceptar')
            return

        self.RegistrarPrestamo(isbn, carnet)
        return 

    def RegistrarPrestamo(self, ISBN, carnet):
        try:
            fecha_prestamo = datetime.now() + timedelta(days=5)
            
            self.BaseDatos.RegistrarPrestamo(ISBN, carnet, fecha_prestamo)
            self.view.Mensaje("El libro se ha prestado con éxito")
            input('Presione cualquier tecla para aceptar')
        except:
            self.view.Mensaje("El libro no se ha prestado")
            input('Presione cualquier tecla para aceptar')
