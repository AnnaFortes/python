#faça um algoritimo que leia o preco de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Valor do produto: '))
desc = int(input('Quantidade de desconto: '))
desconto = (desc / 100) * preco
novoValor = preco - desconto
print(f'O valor com {desc}% de desconto fica \033[33m {novoValor :.2f}\033[m ')