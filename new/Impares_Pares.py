import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

inpares = []
pares = []

clear_screen()

print("podrá ingresar numeros hasta presionar 'p' ")

num = None
while num != "p":
    num = input("Digite um número: ")
    if num == "p" or num == "P":
        break
    try:
        num = int(num)
        if num % 2 == 0:
            pares.append(num)
        else: 
            inpares.append(num)
    except ValueError:
        print("No es un numero válido")

print("\nImpares: ")
for x in range(len(inpares)):
    print(f"{inpares[(x)]}")
print("")
print("\nPares: ")
for x in range(len(pares)):
    print(f"{pares[(x)]}")

