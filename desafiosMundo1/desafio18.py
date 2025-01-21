from random import shuffle
qnt = int(input('Quantos alunos serão cadastrados: '))
alunos = []
for i in range(qnt):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

shuffle(alunos) 

embaralhado = ', '.join(alunos)
print(f'A ordem de apresentação será {embaralhado}')