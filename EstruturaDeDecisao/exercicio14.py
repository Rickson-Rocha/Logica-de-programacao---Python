# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e 
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
primeiraNota = float(input('Insira primeira nota: '))
segundaNota = float(input('Insira segunda nota: '))
media = (primeiraNota+segundaNota)/2

conceitoA = False
conceitoB  = False
conceitoC = False
conceitoD = False
conceitoE = False
conceito = ''
situacaoAp = ''
if media > 9.0 and media <=10.0:
   conceito = 'A'
   conceitoA = True
elif media > 7.5 and media<=9:
   conceitoB = True
   conceito = 'B'
elif media>60 and media<=7.5:
   conceitoC= True
   conceito = 'C'
elif media>4.0 and media<=6.0:
   conceitoD = True
   conceito = 'D'
else:
   if media>=0 and media<=4.0:
      conceitoE = True 
      conceito = 'E'

if conceitoA==True or conceitoB==True or conceitoC==True:
   situacaoAp = 'Aprovado'
else:
   situacaoAp = 'Reprovado'

print('Média de aproveitamento ----- Conceito')
print(f'Notas:{primeiraNota} E  {segundaNota} \n Média: {media} \n Conceito:{conceito} \n Situacao: {situacaoAp}')
