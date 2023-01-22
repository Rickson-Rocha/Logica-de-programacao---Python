#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metro = float(input('m² a serem pintados: '))
litro = metro/3
precoLitro = 80
coberturaLitro = 18

balde = litro/coberturaLitro
totalBaldes = balde*precoLitro

print(f' Para pintar uma área de {metro},você precisará de {balde} de tintas')
print(f'Preco: {totalBaldes}')