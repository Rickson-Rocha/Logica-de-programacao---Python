#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
#  mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo
valorHora = float(input('Valor hora de trabalho: '))
numHora = float(input('Número de horas trabalhadas: '))
salarioBruto = valorHora*numHora
descontoImposto = salarioBruto * (11/100)
descontoInss = salarioBruto * (8/100)
descontoSindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - (descontoImposto + descontoInss + descontoSindicato)
print(f'+ Salário Bruto : R$ {salarioBruto}')
print(f'- IR (11%) : R$ {descontoImposto}')
print(f'- INSS (8%) : R$ {descontoInss}')
print(f'- Sindicato (5%) : R$ {descontoSindicato}')
print(f'= Salário Liquido : R$  {salarioLiquido}')