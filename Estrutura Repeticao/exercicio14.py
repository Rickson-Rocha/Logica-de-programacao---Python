#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
contarImpar = 0 
contarPar = 0
for i in range(10):
    numero = int(input(f'{i+1} número: '))
    if numero%2==0:
        contarPar+=1
    else:
        contarImpar+=1
print(f'Quantidade de números pares : {contarPar} | Quantidade de números ímpares {contarImpar}')

