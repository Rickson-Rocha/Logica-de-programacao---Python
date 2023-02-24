#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Interpretei que esse intervalo é aberto,logo os números colhidos do usuário não aparecerão no print de saida
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
for i in range(n1+1,n2):
    print(i)