def biblioteca_llena(canciones_registradas):
    contador = sum(1 for c in canciones_registradas if c is not None)
    return contador == 15

def main():
    canciones = [None] * 15
    
    while not biblioteca_llena(canciones):
        print("\n1.- Agregar cancion")
        print("2.- Eliminar cancion")
        print("3.- Ver canciones")
        print("4.- Cerrar")

        try:
            menu = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un valor numerico")
            continue
            
        if menu == 1:
            nombre_cancion = input("Nombre de la cancion: ")
            guardado = False
            for i in range(len(canciones)):
                if canciones[i] is None:
                    canciones[i] = nombre_cancion
                    guardado = True
                    break
                
        elif menu == 2:
            nombre_cancion = input("Nombre de la cancion a eliminar: ")
            encontrada = False
            for i in range(len(canciones)):
                if canciones[i] is not None and canciones[i] == nombre_cancion:
                    canciones[i] = None
                    encontrada = True
                    print("Cancion eliminada")
                    break
            if not encontrada:
                print("No se encontro esa cancion")
                
        elif menu == 3:
            hay_canciones = False
            for j in range(len(canciones)):
                if canciones[j] is not None:
                    print(f"{j + 1}. {canciones[j]}")
                    hay_canciones = True
            if not hay_canciones:
                print("La biblioteca esta vacia")
                
        elif menu == 4:
            print("Registro finalizado")
            break
        else:
            print("Ingrese una opcion valida")