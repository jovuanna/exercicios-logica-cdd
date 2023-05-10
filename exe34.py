num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"Esse número é par {num}.")
    '''if num != 0:'''
    if num > 0:
        print("O número é positivo.")
    else:
        print("O número é negativo")
else:
    print(f"Esse número é ímpar {num}.")
