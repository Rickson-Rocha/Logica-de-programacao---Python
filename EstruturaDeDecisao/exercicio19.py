"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

numero = int(input('Insira um número:'))
unidade = numero % 10
numero = (numero - unidade)/10
dezena = numero % 10
numero = (numero - dezena)/10
centena = numero
if numero < 1000:
  if numero>=100:
     print(f'{numero} = {centena}, {int(dezena)} e {unidade}')
  elif numero>=10 and numero<=99:
     print(f'{numero} = {int(dezena)} dezenas e {unidade} unidade(s)') 
  else:
     print(f'{numero} = {unidade} unidades(s)')
else:
    print('O número informado deve ser menor que 1000')




