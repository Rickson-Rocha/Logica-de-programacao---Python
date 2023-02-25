#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numero = []
par = []
impar = []

for i in range(7):
    numeros = int(input(f'{i+1}º: '))
    numero.append(numeros)
    if numeros%2!=0:
        impar.append(numeros)
    else:
        par.append(numeros)

print(f'Lista de números: {numero} \n Lista de números pares: {par} \n Lista de números impares: {impar}')