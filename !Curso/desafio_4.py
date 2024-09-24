def marcar_pares():
    while True:
        numero = int(input("Ingresá un número entero positivo: "))
        if numero >= 0:
            break
        print("Por favor, ingresá un número positivo.")
    
    for i in range(numero + 1):
        if i % 2 == 0:
            print(f"{i} par")
        else:
            print(i)

marcar_pares()
