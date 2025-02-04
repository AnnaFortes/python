soma = cont = 0
menor = None
maisBarato = ''

print('=-' * 20)
print('LOJA REI DA BARATEZA'.center(40))
print('=-' * 20)

while True: 
    produto = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Preço R$ '))

    prosseguir = ''

    while prosseguir not in ('S', 'N'):
        prosseguir = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    
    if prosseguir == 'N':
        print('-' * 8, 'FIM DO PROGRAMA', '-' * 8)
        break
    soma += preco

    if preco > 999:
        cont += 1

    if menor is None or preco < menor:
        menor = preco
        maisBarato = produto

print(f'O total da compra foi R${soma :.2f}')
print(f'Temos {cont} produtos custando mais de R$1000')
print(f'O produto mais barato foi {maisBarato} que custa R${menor :.2f}')
