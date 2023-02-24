#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


numero = int(input('Informe um número qual deseja calcular o fatorial: ')) 
mult = 1
for i in range(1,numero+1):
   mult*= i
print(mult)