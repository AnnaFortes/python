valores = []

for c in range(5): 
    num = int(input('Digite um valor: '))

    if c == 0 or num > valores[-1]: 
        valores.append(num) 
        print('Adicionado ao final da lista...')   
    else:
        pos = 0

        while pos < len(valores): 
            if num <= valores[pos]:
                valores.insert(pos, num) 
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
                
print('=-' * 20)
print(f'Os valores digitados em ordem foram {valores}')
print()
        