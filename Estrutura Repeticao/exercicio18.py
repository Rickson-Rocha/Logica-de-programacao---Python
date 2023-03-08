#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

qtdNumero = int(input('Quantos números deseja fornecer: '))
soma = 0
maiorNumero = 0
menorNumero = 0
for i in range(qtdNumero):
    numero = int(input(f'{i+1}º número: '))
    soma+= numero
    if numero>maiorNumero:
        maiorNumero = numero
    elif menorNumero==0 or numero<menorNumero:
        menorNumero =  numero
print(f'Soma dos valores repassados: {soma}  | Maior número encontrado : {maiorNumero} | menor número encontrado: {menorNumero}')