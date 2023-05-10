medias_alunos = []
outroCalculo = "sim"
while outroCalculo == "sim":
    nota1 = float(input("Digite uma nota: "))
    nota2 = float(input("Digite outra nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média das notas {nota1} e {nota2} é {media}.")
    medias_alunos.append(media)
    if media >= 7:
        print(f"Você foi aprovado! Sua média é {media}.")
    elif media >= 4:
        print(f"Você está em recuperação. Sua média é {media}.")
    else:
        print(f"Você está reprovado. Sua média é {media}.")
    outroCalculo = input("Quer fazer outro calculo? ")
print(medias_alunos)
