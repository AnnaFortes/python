n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m :.1f}')
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')
#como se fosse o ternário do JS
""" if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else: 
    print('Sua média foi ruim, estude mais!') """