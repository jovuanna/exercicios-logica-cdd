resultado = 0
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

while num2 == 0:
    print("Só é permitido número diferente de 0, digite outro número.")
    num2 = float (input())

else:
     resultado = num1 / num2
     print(resultado)
