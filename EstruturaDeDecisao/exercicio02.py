#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input('Digite um valor:'))
if numero>0:
    print(f'{numero}: POSITIVO')
else:
    print(f'{numero} NEGATIVO')

#Nesse caso,para diminuir as linhas de código,pode-se utilizar o operador ternário:
numero = int(input('Digite um valor'))
print(f'{numero} é positivo' if numero>0 else print(f'{numero} é negativo'))