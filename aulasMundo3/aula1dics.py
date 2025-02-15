pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5 #adicionando chaves e valores
for k, v in pessoas.items():#para cada chave em cada valor
    print(f'{k} = {v}')
""" saida: 
           nome = Gustavo
            sexo = M
            idade = 22
            peso = 98.5
    será desse jeito, um embaixo do outro          """