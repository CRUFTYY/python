cadena = input("Ingrese cadena: ")
letra = input("Ingrese la letra a contar: ")

cantidad = 0

for x in range(len(cadena)):
    if letra == cadena[x]:
        cantidad += 1
        print("La letra se repite en la posicion: ", x)

print(f"La letra se reitió: {cantidad} veces")