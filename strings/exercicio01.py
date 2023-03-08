"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."""

print('Compara duas strings')
print()
string_1 = input(' String 1:  ')
string_2 = input(' String 2: ')

print(f'String 1: {string_1}')
print(f'String 2: {string_2}')

tamanho_string_1 = len(string_1)
tamanho_string_2 = len(string_2)

print(f' Tamanho de "{string_1}": {tamanho_string_1} ')
print(f' Tamanho de "{string_2}": {tamanho_string_2} ')

if tamanho_string_1!=tamanho_string_2:
    print('As duas strings têm tamanhos diferentes')
else:
    print('As duas strings têm tamanhos iguais ')

if string_1 == string_2:
    print('As duas strings possuem conteúdo igual')
else:
    print('As duas strings possuem conteúdo diferente')
