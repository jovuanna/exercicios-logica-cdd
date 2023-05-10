continua = "S"
while continua == "S" or continua == "s":
    nota1 = float(input("Insira a primeira nota:"))

    while nota1 < 0 or nota1 > 10:
        print("Valor inválido, digite novamente.")
        nota1 = float(input("Insira a primeira nota:"))

    nota2 = float(input("Insira a segunda nota:"))
    while nota2 < 0 or nota2 > 10:
        print("Valor inválido, digite novamente.")
        nota2 = float(input("Insira a segunda nota:"))
    media = (nota1 + nota2) / 2
    print("A media é: ", media)
    continua = input("Gostaria de calcular para outro aluno? Digite S para Continuar, e N para Encerrar: ")
print("Fim dos cálculos, até mais!")
