num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print("O primeiro número  é maior. ")
    elif num2 > num1 and num2 > num3:
        print("O segundo número é maior. ")
    else:
        print("O terceiro  número é maior.")
else:
    print("Números iguais! Digite números diferentes")
