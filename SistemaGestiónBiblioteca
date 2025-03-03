# Importamos pickle para poder guardar la base de datos en un archivo.
import pickle

# Mostramos título de bienvenida:
print("\nBienvenido al Sistema de Gestión de Biblioteca Ávila Cazorla 3000\n")

# Definimos la clase Libro:


class Libro:
    def __init__(self, titulo, autor, isbn):
        # Inicializamos los atributos del libro:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Que inicialmente está disponible.

    def prestar(self):
        # Creamos un método para prestar el libro:
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')

    def devolver(self):
        # Creamos otro método para devolver el libro:
        if not self.disponible:
            self.disponible = True
            print(f'El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" ya estaba disponible.')

# Definimos la clase GestiónDelInventario:


class GestiónDelInventario:
    def __init__(self):
        # Inicializamos la lista de libros
        self.libros = []

    def agregar(self, titulo, autor, isbn):
        # Creamos método para poder agregar un nuevo libro
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        print(f'Libro agregado con éxito.')

    def mostrar(self):
        # Creamos método para mostrar todos los libros presentes en la base de datos
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(
                f'Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado}')

    def buscar(self, isbn):
        # Método para buscar un libro por ISBN
        for libro in self.libros:
            if libro.isbn == isbn:
                estado = "Disponible" if libro.disponible else "Prestado"
                print(
                    f'Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado}')
                return libro
        print(f'El libro con ISBN {isbn} no está en la base de datos.')
        return None

    def prestar(self, isbn):
        # Método para prestar un libro por ISBN
        libro = self.buscar(isbn)
        if libro:
            libro.prestar()

    def devolver(self, isbn):
        # Método para devolver un libro por ISBN
        libro = self.buscar(isbn)
        if libro:
            libro.devolver()

    def guardar_datos(self, nombre_archivo):
        # Método para guardar los datos en un archivo
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.libros, archivo)
        print(f'Datos guardados en {nombre_archivo}.')

    def cargar_datos(self, nombre_archivo):
        # Método para cargar los datos de un archivo
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.libros = pickle.load(archivo)
            print(f'Datos cargados desde {nombre_archivo}.')
        except FileNotFoundError:
            print(
                f'El archivo {nombre_archivo} no se encontró. Comenzando con una biblioteca vacía.')


# Implementamos el menú con un bucle While

def menu():
    lista = GestiónDelInventario()
    lista.cargar_datos('biblioteca.pkl')
    while True:
        # Mostramos opciones del menú
        print("\nMenú:")
        print("1) Agregar nuevo libro")
        print("2) Prestar libro")
        print("3) Devolver libro")
        print("4) Mostrar libros en la base de datos")
        print("5) Buscar un libro por ISBN")
        print("6) Guardar y salir del programa\n")
        opcion = input("Elige una opción: ").strip()

        # Creamos If para elegir entre las opciones del menú
        if opcion == '1':
            titulo = input("\nTítulo: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            lista.agregar(titulo, autor, isbn)
        elif opcion == '2':
            isbn = input("ISBN del libro a prestar: ")
            lista.prestar(isbn)
        elif opcion == '3':
            isbn = input("ISBN del libro a devolver: ")
            lista.devolver(isbn)
        elif opcion == '4':
            lista.mostrar()
        elif opcion == '5':
            isbn = input("ISBN del libro a buscar: ")
            lista.buscar(isbn)
        elif opcion == '6':
            lista.guardar_datos('biblioteca.pkl')
            print("\nSaliendo de Ávila Cazorla 3000. Gracias por utilizarlo.")
            break
        else:
            print("\nPor favor, elija una opción del menú.")


# Ejecutamos el menú principal
if __name__ == "__main__":
    menu()
