#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# Existem métodos de listas que podem fazer a soma e a multiplicação de seus intens,sem a necessidade fazer outros laços de repetição para atender tais
# finalidades.Porém,irei fazer outro tipo de abordagem,fixando os conceitos de laços de repetição

numero  = []
soma = 0
mult = 1
for i in range(5):
    numeros = int(input(f'{i+1}º número: '))
    numero.append(numeros)

for i in numero:
    soma+=i
print(soma)

for i in  numero:
    mult*=i
print(mult)