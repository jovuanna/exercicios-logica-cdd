continuacao = "sim"
while continuacao == "sim" or continuacao == "Sim" or continuacao == "S" or continuacao == "s":
    num = float(input("Digite um número: "))
    if num == 0:
        print("Erro! Digite um número diferente de 0.")
    elif num > 0:
        print(f"O número {num} é positivo.")
    else:
        print(f"O número {num} é negativo.")
    continuacao = input("Quer continuar a operação? ")
    '''roda o programa de novo até a pessoa digitar não'''
else:
    print("Fim do programa!")
