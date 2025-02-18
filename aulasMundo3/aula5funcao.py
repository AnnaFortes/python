def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 #cada numero de cada posição em lst vai ser multiplicado por 2
        pos += 1 #e adicionado na posição dele mesmo

valores = [6, 3, 9, 1, 0, 2]
dobra(valores) #quando eu chamar o dobra(valores) ele vai subir e dobrar um por um, até acabar e depois vai printar os valores dobrados
print(valores)
""" SAÍDA:
[12, 6, 18, 2, 0, 4]
"""