#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ').lower()
if letra!='a' and letra!='e' and letra !='i' and letra!='u':
    print(f'{letra} é consoante')
else:
    print(f'{letra} é vogal')