produtos = (('Pão de forma', 5), ('Leite', 4), ('Carne moída', 22), ('Frango', 10), ('Salgadinho', 1.60), ('Macarrão', 3.50), ('Suco', 5), ('Refrigerante', 6))
print('-' * 50)
print('LISTAGEM DE PREÇOS'.center(50))
print('-' * 50)

for cont in range(len(produtos)):
    print(f'{produtos[cont][0]:.<42}', end='')
    print(f'R${produtos[cont][1]:>6.2f}')
print('-' * 50)
print()
