from datetime import date
somaMaior = 0
somaMenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 21:
        somaMaior += 1
    elif idade < 21:
        somaMenor += 1
print(f'{somaMaior} pessoas atingiram a maior idade!')
print(f'{somaMenor} pessoas ainda não atingiram a maior idade!')



        
