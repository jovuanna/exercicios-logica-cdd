x = 1
soma = 0 #Faz com que a variável soma comece na repetição zerada
while x <= 10: #a estrutura vai ser verdadeira apenas se a variável "x" for menor ou igual a 10
    n = int(input("Digite um número: "))
    soma = soma + n
    x = x+1 #vai adicionando +1 até parar no 10 e parar a repetição "n = int(input("Digite um número: "))"
media = soma / 10
print(media)
