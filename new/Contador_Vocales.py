def contar_vocales(cadena):
    vocales = "aeiouáéíóú"
    cantidad_vocales = 0
    for letra in cadena:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

cadena = input("Ingrese una palabra: ").lower()
print(f"La palabra tiene {contar_vocales(cadena)} vocales")