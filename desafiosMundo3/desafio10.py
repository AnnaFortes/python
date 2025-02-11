cont = 0
lista = []

while True:
    num = int(input('Digite um número: '))
    
    lista.append(num)

    cont += 1

    continuar = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        print('=-' * 20)
        break
   
print(f'Ao todo foram digitados {cont} números. ')

lista.sort(reverse=True)

print(f'Lista invertida: {lista}')

if 5 in lista: 
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
print()