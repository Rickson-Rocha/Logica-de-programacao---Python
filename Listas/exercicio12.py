"""Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

qtdAluno = 30
altura = []
idadeList = []
alturaList = []
contador = 0

for i in range(qtdAluno):
    print(f'Aluno nº{i+1}º')
    for j in range(1):
        idade = int(input('Idade: '))
        idadeList.append(idade)
        altura = float(input('Altura: '))
        alturaList.append(altura)
    
mediaAltura = sum(alturaList)/qtdAluno

for i in range(len(idadeList)):
    for j in range(len(alturaList)):
        if idade[i]>13 and altura[j]<mediaAltura:
                contador+=1

print(f'Média de altura da turma: {mediaAltura}')
print(f'Total de alunos com 13 anos com altura inferior à média de altura da turma: {contador}')