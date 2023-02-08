# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioAtual = float(input('Informe seu sário R$: '))
if salarioAtual >0 and salarioAtual <= 280:
    novoSalario = salarioAtual + (20/100 * salarioAtual)
    print(f'Seu novo salário é de R${novoSalario}')
elif salarioAtual> 280 and salarioAtual<=700:
      novoSalario = salarioAtual + (15/100 * salarioAtual)
      print(f'Seu novo salário é de R${novoSalario}')
elif salarioAtual> 700 and salarioAtual<=1500:
      novoSalario = salarioAtual + (10/100 * salarioAtual)
      print(f'Seu novo salário é de R${novoSalario}')
else:
     if salarioAtual > 1500:
            novoSalario = salarioAtual + (5/100 * salarioAtual)
            print(f'Seu novo salário é de R${novoSalario}')