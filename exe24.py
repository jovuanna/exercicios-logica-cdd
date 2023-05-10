A = []
M = []

for a in range(10):
    A.append(float(input("Digite um número: ")))
x = float(input("Digite um número para multiplicar: "))

for b in range(10):
    '''M = x * A[b]'''
    M.append(x*A[b])
    '''print(M)'''
print(A)
print(x)
print(M)
