#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora = float(input('Informe valor por hora trabalhada: '))
numHora = float(input('Informe o número de área de trabalhadas '))
#supondo que o indivíduo tenha trabalhado 28 dias no mês
calculo = valorHora*numHora
print(f'Salário R$ {calculo}')