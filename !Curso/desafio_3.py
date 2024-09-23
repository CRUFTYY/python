
diccionario = {}

while True:
    clave = input("Ingresá un nombre (o dejá vacío para terminar): ").lower()
    if clave == "":
        break
    valor = input(f"Ingresá la edad de {clave}: ")
    diccionario[clave] = valor
    print("")


for clave, valor in diccionario.items():
    print(f"{clave}: {valor} años")

print("")
clave_buscar = input("Ingresá el nombre que querés buscar: ").lower()
resultado = diccionario.get(clave_buscar)

print("")
if resultado:
    print(f"{clave_buscar} tiene {resultado} años.")
else:
    print(f"{clave_buscar} no está en el diccionario.")
