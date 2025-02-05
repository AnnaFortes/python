cont = conts = contm = 0

while True: 
    print('-=' * 20)
    idade = int(input('Idade: ')) 

    sexo = ''

    while sexo not in ('M', 'F'):
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    pros = '' 

    while pros not in ('S', 'N'):
        pros = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]

    if pros in 'Nn':
        print('-' * 15)
        print('FINALIZANDO...')
        print('-' * 15)
        break

    if idade > 17:
        cont += 1
    if sexo == 'M':
        conts += 1
    if sexo == 'F' and idade > 19:
        contm += 1

print(f'Ao total {cont} pessoas são maiores de 18 anos.')
print(f'{conts} homens foram cadastrados. ')
print(f'{contm} mulheres são maiores de 20 anos. ')