from math import sin, tan, cos, radians
angulo = int(input('Digite o valor do angulo: ')) #valor do angulo em graus
angulo_radiano = radians(angulo) #convertendo o valor para radiano
print(f'No angulo {angulo}° temos: ')
print(f'Seno com o valor de {sin(angulo_radiano) :.3f} rad')
print(f'Cosseno com o valor de {cos(angulo_radiano) :.3f} rad') 
print(f'Tangente com o valor de {tan(angulo_radiano) :.3f} rad')
