"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

msgParImpar = ' '
msgPositivoNegativo = ''
msgInteiroDecimal = ''

n1 = float(input('N1:'))
n2 = float(input('N2:'))
op = input('Escolha a operação: + | - | * | /')
print(f'Operação escolhida: {op}')
match(op):
    case '+':
        op = n1+n2
    case '-':
        op = n1-n2
    case '*':
        op = n1*n2
    case '/':
        op = n1/n2

#Verificando se o número é inteiro ou decimal
#lembre-se que números decimais não são classificados em par ou ímpar

if op==(op//1):
   msgInteiroDecimal = 'inteiro'
   if op%2==0:
       msgParImpar = 'par'
   else:
       msgParImpar = 'Impar'
else:
    msgInteiroDecimal = 'Decimal'
    msgParImpar = 'Números decimais não são classificados em par ou ímpar'

if op>0:
    msgPositivoNegativo = 'Positivo'
else:
    msgPositivoNegativo = 'Negativo'

print(f'Resultado: {op} \n Classificação: {msgParImpar} \n Classificação: {msgPositivoNegativo}')