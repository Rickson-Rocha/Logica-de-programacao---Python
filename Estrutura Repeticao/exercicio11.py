#Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
soma = 0 
for i in range(n1+1,n2):
    soma+=i
print(f'Soma dos valores inteiros no intervalo ]{n1},{n2}[ | Resultado: {soma}')