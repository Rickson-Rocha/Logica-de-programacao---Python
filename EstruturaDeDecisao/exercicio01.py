#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número'))
if n1==n2:
    print(f'Os números digitados precisam ser diferentes')
else:
    if n1>n2:
        print(f' O maior número digitado : {n1}')
    else:
        print(f'O maior número digitado: {n2}')