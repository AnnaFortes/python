import random
qnt = int(input('Quantos alunos serão sorteados: '))
alunos = []
for i in range(qnt):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

random.shuffle(alunos) 

embaralhado = ', '.join(alunos)
print(f'A ordem sorteada foi {embaralhado}')