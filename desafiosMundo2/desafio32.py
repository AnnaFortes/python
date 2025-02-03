from time import sleep

while True:
    print('=-' * 30 )
    tab = int(input('Quer ver a tabuada de qual valor: [negativo para sair] '))
    sleep(0.5)
    if tab < 0:
        print('=-' * 25)
        print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')  
        print('=-' * 25) 
        break 

    print('=-' * 30 )
    
    for cont in range(1, 11):
        res = tab * cont
        sleep(0.3)
        print(f'{tab} x {cont} = {res}')
    sleep(0.5)
    
    
    
    
