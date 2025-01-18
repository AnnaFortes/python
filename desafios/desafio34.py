#ler o comprimento de 3 retas e diga se elas podem ou não formar um triangulo
reta1 = int(input('Informe o valor da primeira reta: '))
reta2 = int(input('Informe o valor da segunda reta: '))
reta3 = int(input('Informe o valor da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')