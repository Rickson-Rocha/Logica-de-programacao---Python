#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numeros = []
for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
print(numeros)