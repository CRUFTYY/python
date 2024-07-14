#Crea un diccionario que contenga tres pares clave-valor con información sobre una persona (por ejemplo, nombre, edad, y ciudad) y luego imprime cada par en una línea separada.

persona = {

    "nombre":"John",
    "edad": 23,
    "ciudad":"Boston"
 }

for clave, valor in persona.items():
    print(f"{clave}: {valor}")