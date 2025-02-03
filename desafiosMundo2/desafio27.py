print('=-' * 15)
print(' ' * 6, 'TERMOS DE UMA PA')
print('=-' * 15)

termo = int(input('Primero termo: '))
razao = int(input('Razão: '))
n = int(input('Digite o número de termos: '))

while True: 
    cont = 0   
    while cont < n:
        print(termo, end=' -> ')
        termo += razao
        cont += 1

    print('Acabou!')

    escolha = int(input('Você gostaria de escolher alguns termos? \n[1] Continuar: \n[2] Encerrar: '))

    if escolha == 1:
        n = int(input('Quantos termos você gostaria de adicionar? '))
    if n == 0:
            print('FIM!')
            break
    elif escolha == 2:
        print('FIM!')
        break