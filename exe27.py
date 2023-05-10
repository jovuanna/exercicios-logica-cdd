n = int(input("Digite um valor: "))
A = []
B = []
soma = []
for a in range(n):
    A.append(int(input("Digite um número: ")))
    B.append(int(input("Digite outro número: ")))
    soma = A[a] + B[a]
    print(soma)
