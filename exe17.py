print("---Menu---")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print('''1. Soma
         2. Subtração
         3. Multiplicação
         4. Divisão
         5. Para digitar um novo número
         6. Para sair''')

reset = "S"
operacoes = int(input("Selecione as operações: "))
while reset == "S" or reset == "s":
    while operacoes > 0 or operacoes < 7:
        if operacoes == 1:
            soma = num1 + num2
            print(soma)
            break
        elif operacoes == 2:
            subtracao = num1 - num2
            print(subtracao)
            break
        elif operacoes == 3:
            multiplicacao = num1 * num2
            print(multiplicacao)
            break
        elif operacoes == 4:
            divisao = num1 / num2
            print(divisao)
            break
        elif operacoes == 5:
            reset = str(input("Deseja resolver um novo problema? Digite (S) para sim."))
            break
        else:
            print("Encerrando programa...")
            break
