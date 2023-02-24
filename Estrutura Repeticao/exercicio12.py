"""Desenvolva um gerador de tabuada, 
capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""

mult = 1
while True:
    numero = int(input('Digite um número para ser calculado na tabuada: '))
    if numero<1 or numero>10:
        print('Numero informado precisa estar no intervalo [1,10]')
        numero = int(input('Digite um número para ser calculado na tabuada: '))
    else:
     for i in range(1,11):
        mult=numero*i
        print(f'{numero} x {i} = {mult}')
    break