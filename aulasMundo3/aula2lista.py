valores = []

for cont in range(5):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores): #para cada indice e elemento da minha lista
    print(f'Na posição {chave} encontrei o valor {valor}!') 
    
print('Cheguei ao final da lista.')

