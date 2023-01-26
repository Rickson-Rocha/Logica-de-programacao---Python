#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('Digite um número :'))
n2 = int(input('Digite um número :'))
n3 = int(input('Digite um número :'))
if n1>n2>n3 or n1>n3>n2:
    print(f'Menor número: {n1}')
elif n2>n1>n3 or n2>n3>n1:
     print(f'Menor número: {n2}')
else:
    if n3>n2>n1 or n3>n1>n2:
         print(f'Menor número: {n3}')