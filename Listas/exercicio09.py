#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numero = 5
vetorA = []
for i in range(numero):
    n = int(input(f'{i+1}nº: '))
    vetorA.append(n)

somaQuadrado = 0
sQuadrado = []
for i in  vetorA:
    somaQuadrado += +(i**2)
    sQuadrado.append(somaQuadrado)
print(somaQuadrado)