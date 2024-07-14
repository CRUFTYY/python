# Write to the file
with open("archivo.txt", "w") as archivo:
    archivo.write("Primera línea.\n")
    archivo.write("Segunda línea.\n")
    archivo.write("Tercera línea.\n")

# Read from the file
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
