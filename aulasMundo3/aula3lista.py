a = [2, 3, 4, 7]
b = a[:] #uma cópia dos valores, assim ele não cria uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
