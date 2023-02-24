#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

qtdNumero = int(input('Quantos números deseja fornecer considerando o intervalo [0,100]: '))
soma = 0
maiorNumero = 0
menorNumero = 0
for i in range(qtdNumero):
    if qtdNumero<0 or qtdNumero>100:
        print('Valor fornecido fora do intervalo [0,100]')
        break
    else:

        numero = int(input(f'{i+1}º número: '))
        soma+= numero
        if numero>maiorNumero:
            maiorNumero = numero
        elif menorNumero==0 or numero<menorNumero:
            menorNumero =  numero
    print(f'Soma dos valores repassados: {soma}  | Maior número encontrado : {maiorNumero} | menor número encontrado {menorNumero}')