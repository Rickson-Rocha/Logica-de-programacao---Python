#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(4):
    nota = float(input(f'{i+1} nota: '))
    notas.append(nota)
media = sum(notas)/len(notas)
print(f'Média: {media}')