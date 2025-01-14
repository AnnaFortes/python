#um professor quer sortear um dos seu alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo no nome dos escolhidos
import random
qnt = int(input('Quantos alunos deseja cadastrar: '))
alunos = []
for i in range(qnt):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
escolha = random.choice(alunos)
print(f'O aluno escolhido foi {escolha}')
    