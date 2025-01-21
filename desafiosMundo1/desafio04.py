#crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2) #ou pow(numero, (1/2))
print(f'Dobro: \033[35m{dobro}\n\033[m\nTriplo: \033[32m {triplo}\033[m \nRaiz:\033[34m{raiz :.2f}\033[m ') 