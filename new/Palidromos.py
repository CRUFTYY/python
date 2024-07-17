import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def palidromo(cadena):
    cadena = cadena.lower()
    cadena_temporal = cadena[::-1]
    if cadena == cadena_temporal:
        return True
    else:
        return False
clear_screen()

cadena = str(input("Ingrese una cadena: "))

if palidromo(cadena):
    print("La cadena es palídromo")
else:
    print("La cadena no es un palídromo")