notas = []

while True:
    boletim = []
    soma = 0

    aluno = str(input('Nome: ')).strip().upper()
    boletim.append(aluno)

    for n in range(2):
        nota = float(input(f'Nota {n + 1}: '))
        boletim.append(nota)
        soma += nota 

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
    print(f'{i+1:<4}{aluno[0]:<15}{aluno[-1]:>6.1f}')
print('-'*35)
print()
   

