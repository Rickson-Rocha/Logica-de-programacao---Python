# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
#Imprima a idade e a altura na ordem inversa a ordem lida.
coletas = 2
dados = 1
lista= []
for i in range(coletas):
  for j in range(1):
    idade = int(input(f' Pessoa nº {i+1}; Idade: '))
    altura = float(input(f' Pessoa nº {i+1}; Altura: '))
    lista.append([altura,idade])
print(lista)

#imprindo na ordem inversa
print(list(reversed(lista)))