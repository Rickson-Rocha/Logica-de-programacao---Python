"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litrosVendidos = float(input('Total de litros vendidos: '))
tipoCombustivel = input('Combustivel: A-álcool, G-gasolina ').lower()
precoAlcool = 1.90
precoGasolina = 2.50
if tipoCombustivel=='a':
    if litrosVendidos<=20:
        porcentagemL = precoAlcool - (precoAlcool * (3/100))
        calculoPagar = litrosVendidos * porcentagemL
    else:
        porcentagemL = precoAlcool - (precoAlcool * (5/100))  
        calculoPagar = litrosVendidos * porcentagemL
else:
    if tipoCombustivel=='g':
      if litrosVendidos<=20:
            porcentagemL = precoAlcool - (precoAlcool * (4/100))
            calculoPagar = litrosVendidos * porcentagemL
      else:
            porcentagemL = precoAlcool - (precoAlcool * (6/100))  
            calculoPagar = litrosVendidos * porcentagemL