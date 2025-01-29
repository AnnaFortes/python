#ler um numero e ler seu fatorial
c = 1
num = int(input('Digite um número: '))
while num > c:
    c = num -1
    num *= c
print(num)
