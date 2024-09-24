def marcar_pares(numero):
    if numero < 0:
        print("El número debe ser entero positivo.")
        return

    for i in range(numero + 1): 
        if i % 2 == 0:  
            print(f"{i} par")
        else:  
            print(i)


while True:
    numero_ingresado = int(input("Ingresá un número entero positivo: "))
    if numero_ingresado >= 0: 
        break
    print("Por favor, ingresá un número positivo.")

marcar_pares(numero_ingresado)
