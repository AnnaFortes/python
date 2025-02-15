estado = {}
brasil = []

for c in range (3):
    estado['uf'] = str(input('Unidade Feterativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #copiando para não haver repetições
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
""" saida:
Unidade Feterativa: Acre
Sigla do estado: AC
Unidade Feterativa: Amazonas
Sigla do estado: AM
Unidade Feterativa: Pará
Sigla do estado: PA
Acre AC 
Amazonas AM
Pará PA
"""