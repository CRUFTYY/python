import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def celsius_a_fahrenheit(celsius):
    return (9/5 * celsius) + 32
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

clear_screen()

opcion = input("Ingrese una opcion: \n celsius a fahrenheit (a) \n fahrenheit a celsius (b)\n").lower()

try:
    if opcion == "celsius a fahrenheit" or opcion == "a":
        celsius = float(input("Ingrese grados celsius a convertir: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{fahrenheit} Grados Fahrenheit")

    elif opcion == "fahrenheit a celsius" or opcion == "b":
        fahrenheit = float(input("Ingrese grados fahrenheit a convertir: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{celsius} Grados Celsius")
except ValueError:
    print("opcion incorrecta, ingrese una opcion válida. ")
