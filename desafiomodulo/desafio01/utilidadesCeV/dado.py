def lerDinheiro(msg):
    while True:
        preco = input(msg).strip().replace(',', '.') #remove espaços em branco, troca , por .
        if preco.replace('.', '', 1).isdigit(): #verifica se é um numero(com um unico (.)ponto)
            return float(preco) 
        else:
            print(f'\033[31mERRO! Digite um número!\033[m')
        
