notas = []
soma = 0
cont = 0
for a in range(5):
    notas.append(float(input("Digite uma nota: ")))
for b in range(5):
    soma += notas[b]
media = soma / 5
for c in range(5):
    if notas[c] >= media:
        cont += 1
print(cont)
