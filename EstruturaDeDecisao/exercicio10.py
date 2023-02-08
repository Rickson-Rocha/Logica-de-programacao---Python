#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Informe em qual turno você estuda:  \n |M - Matutino , V - Vespertido | N - Noturno : ' ).lower()
if turno!='m' and turno!='v' and turno!='n':
    print('Turno inválido')
else:
    if turno=='m':
        print('Bom dia')
    if turno=='v':
        print('Boa tarde')
    if turno=='n':
        print('Boa noite')