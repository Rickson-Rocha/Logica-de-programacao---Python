#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for i in range(1,51):
 print(f'{i}',end=",") if i%2!=0 else i