class Calculadora:

    def mostrarMenu(self):
        decision = 0
        while decision != 5:
            print("======================")
            print("CALCULADORA SIMPLE")
            print("Escoga una operacion.")
            print("1.- Sumar")
            print("2.- Restar")
            print("3.- Multiplicar")
            print("4.- Dividir")
            print("5.- Cerrar")
            decision = int(input("Operacion: "))
            if decision == 5:
                print("Proceso terminado.")
                break
            if 1 <= decision <= 4:
                numero1 = float(input("Ingrese el primer numero: "))
                numero2 = float(input("Ingrese el segundo numero: "))
                resultado = 0
                if decision == 1:
                    resultado = numero1 + numero2
                elif decision == 2:
                    resultado = numero1 - numero2
                elif decision == 3:
                    resultado = numero1 * numero2
                elif decision == 4:
                    if numero2 == 0:
                        print("No se puede dividir entre cero.")
                        continue
                    else:
                        resultado = numero1 / numero2
                print(f"Resultado: {resultado}")
            else:
                print("Ingrese una opcion valida.")
                
calc = Calculadora()
calc.mostrarMenu()