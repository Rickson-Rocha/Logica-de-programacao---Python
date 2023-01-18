#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
tempFah = float(input('Informe a temperatura Fº :'))
converC =  5 * ((tempFah-32)/9)
print(f'{converC}º')