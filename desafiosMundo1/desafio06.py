#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
#km, hectometro, decametro, decimetro
numero = int(input('Digite o valor em metros: '))
km = numero / 1000
hm = numero / 100
dam = numero / 10
dm = numero * 10
cm = numero * 100
mm = numero * 1000
print(f'{numero} metros em \nCentimetros: {cm} \nMilímetros: {mm} \nKilometros: {km} \nHectometro: {hm} \nDecametro: {dam} \nDecimetro: {dm}')