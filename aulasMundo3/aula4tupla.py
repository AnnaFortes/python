pessoa = ('Gustavo', 39, 'M', 99.88) #o tipo de dado não interfere a TUPLA
del(pessoa[0]) #apagando a variavel da memória(serve para qualquer coisa dentro do Python)
print(pessoa) #saida: erro, TypeError: 'tuple' object doesn't support item deletion, não posso deletar somente um item na tupla, somente ela toda