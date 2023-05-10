'''quant_alunos = int(input("Quantos alunos tem na sala? "))
alunos = []
for a in range (quant_alunos):
    alunos.append(input("Digite um nome: "))
    '''
print("-"*10, "MOSTRAR A POSIÇÃO DO ARRAY", "-"*10)
alunos = int(input(" Quantos alunos têm na sala: "))
turma = []
#lista vazia que vai ser preenchida no próximo for
for x in range(alunos):
    turma.append(input("Digite o nome de cada aluno: "))
#.append adiciona um elemento ao final da lista
for z in range(alunos):
    print(turma[z], z)
#imprime a lista e a posição
