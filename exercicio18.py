ano = int(input('Informe um ano: XXXX: '))
calculo = ano/4
if int(calculo)==calculo:
    print(f'{ano} \n classificação: Bissexto')
else:
    print(f'{ano} \n classificação: Ano não bissexto')