#ler uma frase e dizer quantas vezes aparece a letra a, em que posição ela aparece a primeira vez e a posição que aparece a ultima vez
frase = input('Digite uma frase: ').lower()
posicao1 = frase.index('a')
posicaoul = frase.rindex('a')
print(f'Tem a letra a na frase: {'a' in frase[:]}')
print(f'A primeira vez em que a letra a aparece é na posição: {posicao1}')
print(f'A ultima vez em que a letra a aparece é na posição: {posicaoul}')
