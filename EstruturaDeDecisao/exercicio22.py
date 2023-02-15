numero =  int(input('Digite um número: '))
if numero == 0:
    print(f'numero informado precisa ser diferente de 0')
else:
    print(f'{numero} é par'if numero%2==0 else print(f'{numero} é ímpar'))
