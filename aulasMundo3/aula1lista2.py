teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) #fazendo uma cópia eu só mudo uma estrutura
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera) #saida: [['Gustavo', 40], ['Maria', 22]]