#Faça um Programa que peça as quatro notas de 10 alunos, 
#calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nomeAluno = []
medias = []
contadorMedia = 0
for i in range(2):
    nome = input(f'{i+1}º Aluno: ')
    nomeAluno.append(nome)
    somador = 0
    media = 0
    for j in range(4):
        notas = float(input(f'{j+1} nota do aluno {nome}: '))
        somador+=notas
    media = somador/4
    medias.append(media)
    if media>7:
         contadorMedia+=1


for i in range(len(nomeAluno)):
    print(f'{nomeAluno[i]} {medias[i]}')

print(f'Número de aluno(s) com media maior ou igual a 7: {contadorMedia}')