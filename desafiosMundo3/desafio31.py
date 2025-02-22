def fat(num=1, show=False):
    f = 1
    if show:
        print(f'Calculando o fatorial de {num}!', end=' = ')

    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    
    if show:
        print(f)
    return f

    
resultado = fat(5, show=False)
print(resultado)
