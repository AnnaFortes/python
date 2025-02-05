lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for pos, comida in enumerate(lanche): 
    print(f'Eu vou comer {comida} na posição {pos}') #comida seria os elementos e pos a posição, enumerate() sempre retorna (índice, valor)
    
""" for cont in range(0, len(lanche)): 
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #assim pegamos o elemento do indice e se eu precisar da posição... """
print('Comi pra caramba!')

