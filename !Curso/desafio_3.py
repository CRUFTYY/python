import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

diccionario = {}

nombre_clave = input("Ingresá el nombre de la clave : ")
nombre_valor = input("Ingresá el nombre del valor : ")


while True:
    clave = input(f"Ingresá un {nombre_clave} (o dejá vacío para terminar): ").lower()
    if clave == "":
        break
    valor = input(f"Ingresá la {nombre_valor} de {clave}: ").lower()
    diccionario[clave] = valor
    print("")


for clave, valor in diccionario.items():
    print(f"{clave}: {valor} {nombre_valor}")

print("")

clave_buscar = input(f"Ingresá el {nombre_clave} que querés buscar: ").lower()

print("")
if clave_buscar in diccionario:
    print(f"{clave_buscar} tiene {diccionario[clave_buscar]} {nombre_valor}.")
else:
    print(f"{clave_buscar} no está en el diccionario.")
