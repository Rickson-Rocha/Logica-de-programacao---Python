""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 """

aH = float(input('Homem - Digite sua altura :'))
calculoAh = (72.7*aH) - 58
print(f'Seu peso ideal é : {calculoAh}')

aM = float(input('Mulher - Digite sua altura :'))
calculoAm = (62.1*aM) - 58
print(f'Seu peso ideal é : {calculoAm}')