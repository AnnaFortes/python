cont = 0
a = 0
b = 1

num = int(input('Digite o valor final da sequencia FIBONACCI: '))

print(f'{a} - {b}', end='')
cont = 2 
while cont < num:
    c = a + b 
    a = b 
    b = c 
    print(f' - {c}', end='')
    cont += 1
    

    
