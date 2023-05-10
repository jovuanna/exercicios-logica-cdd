'''vezes = 0
senha1 = 123456
senha2 = int(input("Digite a senha: "))
while senha2 == senha1:
    print("Senha certa!")
    break
else:
    print("Senha errada!")
vezes += 1
print("Sua senha está bloqueada!")'''

pin = "123456"
tentativas = 0 #contador
senha = input("Digite a senha: ")

while senha != pin:
    print("Senha incorreta, digite a senha novamente: ")
    senha = input() #puxa o input pro print anterior
    tentativas = tentativas + 1
    if tentativas > 2:
        print("Senha bloqueada")
        break #para o looping
    else:
        print("Acesso liberado!")