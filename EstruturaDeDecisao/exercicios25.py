#Para resolver essa questão,usurei estrutura de repetição e listas com intuito de deixar o código menos poluído. Essa maneira de resolver
#Não irá prejudicar a lógica contida na estrutura de decisão (tópico abordado no momento)

contadorS=0
contadorN=0
perguntas = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para vítima?','Já trabalhou com a vítima?']
for pergunta in perguntas:
    resposta = input(f'{pergunta} : S\N: ').lower()
    match(resposta):
        case 's':
           contadorS+=1
        case 'n':
            contadorN+=1
        case _:
            print('Resposta inválida.Tente novamente.')
            resposta = input(f'{pergunta} : S\N: ').lower()
if contadorS<=2:
    print('Suspeito')
elif contadorS>2 and contadorS<=4:
    print('Cúmplice')
else:
    print('Assassino')