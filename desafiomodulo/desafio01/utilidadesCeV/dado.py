def lerDinheiro(msg):
    while True:
        preco = input(msg).strip().replace(',', '.') 
        if preco.replace('.', '', 1).isdigit(): 
            return float(preco) 
        else: 
            print(f'\033[31mERRO! Digite um número!\033[m')
        
