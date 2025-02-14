notas = []

while True:
    boletim = []
    soma = 0

    aluno = str(input('Nome: ')).strip().upper()
    boletim.append(aluno)

    somenteNotas = []

    for n in range(2):
        nota = float(input(f'Nota {n + 1}: '))
        soma += nota
        somenteNotas.append(nota)

    boletim.append(somenteNotas)  
    media = soma / 2
    boletim.append(media)
    notas.append(boletim)

    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print('=-' * 25)
print(f'{"N°"} {"NOME":<15} {"MÉDIA":>6}')
print('-'*35)

for i, aluno in enumerate(notas):
    print(f'{i:<4}{aluno[0]:<15}{aluno[-1]:>6.1f}')
print('-'*35)

while True:
    mostrar = int(input('Mostrar nota de qual aluno? (999 interrompe): '))

    if mostrar == 999:
        break

    for i, aluno in enumerate(notas):
        if mostrar == i:
            print(f'Notas de {aluno[0]} são {aluno[1]}')

print('FINALIZANDO...')
print('<<<<< VOLTE SEMPRE >>>>>')
print()
   

