#crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2) #ou pow(numero, (1/2))
print(f'Dobro: {dobro}\nTriplo: {triplo} \nRaiz: {raiz :.2f}') 