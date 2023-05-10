numeros = []
soma = 0
cont1 = 0
cont2 = 0
#numero par no vetor
for a in range(5):
    numeros.append(int(input("Digite um valor: ")))
for b in range(5):
    if numeros[b] % 2 == 0:
        cont1 += 1
        print(f"Esse número é par {numeros[b]}")
#quantidade de número maior no vetor
for x in range(5):
    soma = soma + numeros[x]
print(soma)
media = soma / 5
print(media)
for y in range(5):
    if numeros[y] > media:
        cont2 += 1
print(f"A quantidade de números maiores que a média dentro do vetor é {cont2}.")
