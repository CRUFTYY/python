import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def suma(a, b): 
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("No se puede dividir por 0")
        return None
    else:
        return a / b


while True:
    clear_screen()
    eleccion = input("Ingrese una operación \n Suma(a), Resta(b), Multiplicacion(c), Division(d), Salir ()").lower()

    if eleccion == "salir" or eleccion == "e":
        print("Saliendo de la calculadora...")
        break 

    if eleccion in ["suma", "a", "resta", "b", "multiplicacion", "c", "division", "d"]:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo valor: "))   

        if eleccion == "suma" or eleccion == "a":
            print("Suma")
            print(f"Resultado de la suma: {suma(a, b)}")
        elif eleccion == "resta" or eleccion == "b":
            print("Resta")
            print(f"Resultado de la resta: {resta(a, b)}")
        elif eleccion == "multiplicacion" or eleccion == "c":
            print("Multiplicacion")
            print(f"Resultado de la multiplicacion: {multiplicacion(a, b)}")
        elif eleccion == "division" or eleccion == "d":
            print("Division")
            resultado = division(a, b) 
            if resultado is not None:
                print(f"Resultado de la division: {resultado}")
        input("Presione Enter para continuar")    

    else:
        print("Operación inválida. Por favor, intente de nuevo.")
        input("Presione Enter para continuar...")       

        
