"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de
 a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

import math
#importando o módulo math para usar o método sqrt para extrair raiz de um número 

coeficienteA = int(input('Digite o valor de coeficiente A: '))
if coeficienteA!=0:
    coeficienteB = int(input('Digite o valor de coeficiente B:'))
    coeficienteC = int(input('Digite o valor de coeficiente C:'))
    calculoDelta = (coeficienteB)**2 - 4*coeficienteA*coeficienteC
    if calculoDelta > 0:
        x1 = ((-coeficienteB) + math.sqrt(calculoDelta))/2*coeficienteA
        x2 = ((-coeficienteB) - math.sqrt(calculoDelta))/2*coeficienteA
        print(f'x1={x1} x2={x2} ')
    elif calculoDelta==0:
         x1 = ((-coeficienteB) + math.sqrt(calculoDelta))/2*coeficienteA
         print(f'x1={x1} ')
    else:
        print('Valor de Delta negativo. Programa encerrado')

else:
    print('Valor de A não pode ser  0. Programa encerrado')