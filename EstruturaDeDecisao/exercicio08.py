# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input('Preço 1º produto: '))
p2 = float(input('Preço 2º produto: '))
p3 = float(input('Preço 3º produto: '))
if p1<p2<p3 or p1<p3<p2:
    print('Comprar produto 1')
if p2<p1<p3 or p2<p3<p1:
     print('Comprar produto 2')
if p3<p1<p2 or p3<p2<p1:
      print('Comprar produto 3')