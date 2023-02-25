#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


caracteres= []
vogais = ['a','e','i','o','u']
consoantes = []

for i in range(5): 
    caracter = input(f'{i+1}º caracter: ')   
    caracteres.append(caracter)

for i in caracteres:
    if i in vogais:
        continue
    else:
        consoantes.append(i)

#contando consoantes
qtd = 0
for i in consoantes:
    qtd+=1
  
print(f'Total de consoantes detectadas: {qtd} | Sendo elas: {consoantes}')