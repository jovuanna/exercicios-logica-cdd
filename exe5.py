numero = int(input("Digite um número: "))
contador = 1
for a in range(10):
    a = a * numero
    print(numero, "X", contador, "=", a)
    contador += 1
