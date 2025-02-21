def teste(b):
    global a #qualquer alteração feita dentro da função, afetará a variavél global, então o A global passa a valer 8, mas não afeta o valor passado como parametro, B continua sendo uma copia de A global
    a = 8
    b += 5
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

""" saída:
A dentro vale 8
B dentro vale 10
C dentro vale 2
A fora vale 5
"""