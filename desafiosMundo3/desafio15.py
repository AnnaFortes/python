matriz = [] 

for l in range(0,3):
    linha = [] 
    for c in range(0, 3): 
        valor = int(input(f'Digite um valor para [{l}][{c}]: '))
        linha.append(valor) 
    matriz.append(linha)

print('=-' * 25)
for linha in matriz: 
    for valor in linha: 
        print(f'[{valor:^4}]', end=' ') 
    print() 
