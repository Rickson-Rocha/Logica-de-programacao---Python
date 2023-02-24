""""Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

while True:
  try: nota =  int(input('Digite uma nota : '))
  except ValueError:
    print('Nota inválida. Digite um número inteiro')
  else:
    if nota>=0 and nota<=10:
      print(nota)
      break;