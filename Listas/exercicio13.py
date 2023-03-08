# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
#(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

mesesDoAno = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outuro','novembro','dezembro']
tempeturaMedia = []

for i in  mesesDoAno:
    temperaturaMensal = int(input(f'Informe temperatura do mês de {i}: '))
    tempeturaMedia.append(temperaturaMensal)

mediaAnual = sum(tempeturaMedia)/12
print(mediaAnual)

def verificador(temp):
    if temp > mediaAnual:
        return True
    else:
        False

dadosFiltrados = list(filter(verificador,tempeturaMedia))
print(dadosFiltrados)

