from time import sleep

def contador(incio, fim, passo):
    for c in range(incio, fim, passo):
        print(f'{c}', end=' ', flush=True) 
        sleep(0.2)
    print('FIM!')

def linha():
    print('~' * 40)


linha()
print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 11, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2: ')
contador(10, 0, -2)
linha()

print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

linha()
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

if passo == 0:
    passo = 1

if inicio > fim and passo > 0:
    passo = -passo

elif inicio < fim and passo < 0:
    passo = -passo

for p in range(inicio, fim + (1 if passo > 0 else -1), passo):
    print(f'{p}', end=' ', flush=True)
    sleep(0.2)
print('FIM!')
print()

    
