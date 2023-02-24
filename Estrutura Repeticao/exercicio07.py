#Faça um programa que leia 5 números e informe o maior número.

#Para resolver essa questão,há diversas possibilidades. Destaco duas delas:

#1) Criar uma variável para receber o maior número - incialmente essa variável recebe 0 - e fazer comparações diretas com valores recebidos a cada laço

maiorNumero = 0
for i in range(5):
    numero = int(input(f'{i+1}º número: '))
    if numero > maiorNumero:
        maiorNumero =  numero
print(f'Maior número encontrado: {maiorNumero}')

#2) Criar uma lista parece receber os 5 números e logo após aplicar a função Max que retorna o maior valor da lista
numeros = []
for i in range(5):
    numero = int(input(f'{i+1}º número: '))
    numeros.append(numero)

maiorValor = max[numeros]
print(f'Maior valor econtrado: {maiorValor}')