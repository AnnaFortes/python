def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

#programa principal
soma(b = 4, a = 5) 
soma(7, 2)
soma(3, 9, 5) #ERRO, se eu passo para função que são dois parametros, eu preciso colocar somente 2
""" SAIDA:
A = 5 e B = 4
A soma de A + B = 9
A = 7 e B = 2
A soma de A + B = 9

soma(3, 9, 5)
TypeError: soma() takes 2 positional arguments but 3 were given
 """

