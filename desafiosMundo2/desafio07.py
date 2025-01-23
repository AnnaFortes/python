l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento:'))
form = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 
if form == True: 
    if l1 == l2 == l3:
        print('Formam um triângulo, EQUILATERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Formam um triângulo, ISÓCELES!')
    else:
        print('Formam um triângulo, ESCALENO!') 
else: 
    print('Os lados não formam um triângulo!')
