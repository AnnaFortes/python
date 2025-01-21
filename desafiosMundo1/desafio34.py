reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')