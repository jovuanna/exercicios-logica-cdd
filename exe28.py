numeros = []
cont = 0
for a in range(10):
    numeros.append(int(input("Digite um número: ")))
procure_numero = int(input("Digite um numero para procurar na lista: "))
for b in range(10):
    if procure_numero == numeros[b]:
        cont += 1
print(cont)
