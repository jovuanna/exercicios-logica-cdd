nome = []
senha = []
for a in range(5):
    nome.append(input("Usuário: "))
    senha.append(input("Senha: "))
cont = 0
usuario = input("Digite o seu nome de usuário: ")
senha_usuario = input("Digite a sua senha: ")
for b in range(5):
    '''print(f"O usuário {nome[b]} tem a senha {senha[b]} na posição {b}.")
    - no print tem que pegar a variável do segundo for (b).'''
    if usuario == nome[b] and senha_usuario == senha[b]:
        print("Login efetuado com sucesso!")
        break
    else:
        cont += 1
        '''flag (sinalizador)'''
if cont == 5:
    print("Este usuário não existe!")
