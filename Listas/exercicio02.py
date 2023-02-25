#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numeros = []
numerosInverso = []
for i in range(10):
    numero =  int(input(f'{i+1}º número: '))
    numeros.append(numero)

print(f' lista números na ordem natural {numeros}')

for i in numeros:
    numerosInverso.append(numeros[-i])
print(f'lista números na ordem inversa: {numerosInverso}')
