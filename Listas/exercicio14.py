"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""
pergunta = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']
contS = 0

for perguntas in pergunta:
    respostas =  input(f'{perguntas} | [s] | [n]: ').lower()
    if respostas=='s':
        contS+=1

if contS==2:

    print('Suspeito')

elif contS>2 and contS<=4:
    print('Cumplice')

elif contS==5:
    print('Assasino')
else:
    print('Inocente')
