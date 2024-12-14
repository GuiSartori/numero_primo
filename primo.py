#Versão 5.0

num=100
count = 0

for i in range (1,num+1):
    if num%i == 0:
        count += 1
print(count)
if count == 2:
    print(f'{num} é um número primo.') #Exercício