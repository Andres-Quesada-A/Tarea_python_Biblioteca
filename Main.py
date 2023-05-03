from BaseDatos import BaseDatos
from ControllerPrestamo import ControllerPrestamo
from Estudiante import Estudiante
from Libro import Libro
from ViewPrestamo import ViewPrestamo
import random




View = ViewPrestamo()
DataBase = BaseDatos()




titulos = ["Cien años de soledad", "El amor en los tiempos del cólera", "La ciudad y los perros", "La casa verde",
           "Rayuela", "Ficciones", "El Aleph", "Los pasos perdidos", "El túnel", "Sobre héroes y tumbas"]
autores = ["Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Jorge Luis Borges",
           "Alejo Carpentier", "Ernesto Sabato", "Pablo Neruda", "Isabel Allende", "Garcilaso de la Vega",
           "Octavio Paz"]
# Cargar Libros
for i in range(10):
    ISBN = i + 1
    titulo= titulos[i]
    autor= autores[i]
    edicion = random.randint(1, 5)
    disponibilidad = True
    # self, ISBN, titulo, autor, edicion, disponibilidad
    libro = Libro(ISBN, titulo, autor, edicion, disponibilidad)
    DataBase.agregarLibro(libro)


nombres = ["Juan", "Maria", "Pedro", "Luisa", "Miguel", "Ana", "Lucia", "Jose", "Sofia", "Gabriel"]
carnets = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234, 812345]
for i in range (10):
    estudiante_nuevo = Estudiante(nombres[i], carnets[i])
    DataBase.agregarEstudiante(estudiante_nuevo)


controlador = ControllerPrestamo(View, DataBase)
controlador.EjecutarPrograma()