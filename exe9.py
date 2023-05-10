alunos = int(input("Quantos alunos: "))
a = 1 #a contagem vai começar com 1
soma = 0
while a <= alunos: #a contagem da variável "a" vai até a quantidade declarada para a variável "alunos"
    notas = float(input("Digite as notas: "))
    soma = soma + notas
    a = a+1 #a cada repetição ele aumenta um
media = soma / alunos
print("A média das notas dos alunos é igual a: ", media)
