print("-"*10, "MOSTRAR A POSIÇÃO DO ARRAY", "-"*10)
alunos_quantidade = int(input(" Quantos alunos têm na sala: "))
#quantidade de elementos na lista
turma = []
#lista vazia que vai ser preenchida no próximo for
for a in range(alunos_quantidade):
    turma.append(input("Digite o nome de cada aluno: "))
#.append adiciona um elemento ao final da lista (vai adicionar os nomes à lista vazia turma.)
for b in range(alunos_quantidade):
    print(turma[b], b)
#imprime a lista e a posição

nome_pesquisa = input("Digite um nome para pesquisar: ")
cont = 0
for c in range(alunos_quantidade):
    if nome_pesquisa == turma[c]:
        #se a o nome recebido na variável nome_pesquisa existir no array turma, vai printar a posição
        # e qual o nome que corresponde à ela
        print(c, turma[c])
    else:
        cont += 1
        #se não encontrar o nome digitado, o contador vai fazer com que ele procure todas as vez e mostre que não foi
        # encontrado apenas uma vez.
if cont == alunos_quantidade:
    print("Aluno não encontrado!")
