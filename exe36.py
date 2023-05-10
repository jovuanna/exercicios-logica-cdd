num = int(input("Digite um número: "))
if num < 0:
    num += 1
    print(f"O antecessor é {num}")
else:
    num -= 1
    print(f"O antecessor é {num}")
