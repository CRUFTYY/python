def suma_tres_numeros(num1, num2, num3):
    return num1 + num2 + num3

def resta_flotantes(num1, num2):
    return num1 - num2

def evaluar_numeros(num1, num2):
    if num1 > num2:
        print(f"El mayor es: {num1}")
        print(f"El menor es: {num2}")
    elif num1 < num2:
        print(f"El mayor es: {num2}")
        print(f"El menor es: {num1}")
    else:
        print("Los números son iguales.")


a = int(input("Ingresa el primer número entero para la suma: "))
print("")
b = int(input("Ingresa el segundo número entero para la suma: "))
print("")
c = int(input("Ingresa el tercer número entero para la suma: "))

resultado_suma = suma_tres_numeros(a, b, c)
print(f"La suma de {a}, {b} y {c} es: {resultado_suma}")


x = float(input("Ingresa el primer número flotante para la resta: "))
print("")
y = float(input("Ingresa el segundo número flotante para la resta: "))
resultado_resta = resta_flotantes(x, y)
print(f"La resta de {x} y {y} es: {resultado_resta}")


num1 = int(input("Ingresa el primer número entero para evaluar: "))
print("")
num2 = int(input("Ingresa el segundo número entero para evaluar: "))
evaluar_numeros(num1, num2)
