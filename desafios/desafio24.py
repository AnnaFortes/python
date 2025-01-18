#ler uma frase e dizer quantas vezes aparece a letra a, em que posição ela aparece a primeira vez e a posição que aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip().lower()
posicao1 = frase.index('a')
posicaoul = frase.rindex('a')
print(f'Quantas vezes aparece letra A na frase: {frase.count('a')}')
print(f'A primeira vez em que a letra A aparece é na posição: {posicao1}')
print(f'A ultima vez em que a letra A aparece é na posição: {posicaoul}')
