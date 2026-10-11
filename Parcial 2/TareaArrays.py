libros_titulos = []
libros_autores = []

cantidad = int(input("¿Cuántos libros va a registrar? "))
print("Ingrese el nombre de los libros y sus respectivos autores:")

for libro in range(cantidad):
    print("Libro", libro + 1)
    entradaTitulo = input("Título: ")
    libros_titulos.append(entradaTitulo)
    entradaAutor = input("Autor: ")
    libros_autores.append(entradaAutor)

print("Libros registrados:")
for registro in range(cantidad):
    print(f"Autor: {libros_autores[registro]} Título: {libros_titulos[registro]}")
