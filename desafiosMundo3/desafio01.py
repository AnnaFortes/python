num = (
    (0, 'zero'), (1, 'um'), (2, 'dois'), (3, 'tres'), (4, 'quatro'),(5, 'cinco'), (6, 'seis'), (7, 'sete'), (8, 'oito'), (9, 'nove'), (10, 'dez'), (11, 'onze'), (12, 'doze'), (13, 'treze'), (14, 'quatorze'), (15, 'quinze'), (16, 'dezesseis'), (17, 'dezessete'), (18, 'dezoito'), (19, 'dezenove'), (20, 'vinte')
       )
while True:  
    inteiro = int(input('Digite um número entre 0 e 20: '))
    if inteiro >= 0 and inteiro <= 20:
        break

for cont in range(len(num)): 
    if inteiro == num[cont][0]:
        print(f'Você digitou o número {num[cont][1]}') 