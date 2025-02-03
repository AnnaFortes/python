fat = 1
num = int(input('Digite um número: '))

print(num,'! = ', num, end="")

while num > 1:
    fat *= num 
    num -= 1
    print(f' x {num}', end="")
    
print(f' = {fat}')





    

