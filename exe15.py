n= int(input("Insira um número:"))

for x in range(n+1):
    for y in range(x):
        print(y, end=" ")
    print()