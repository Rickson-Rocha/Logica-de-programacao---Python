"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
 nome =  input('Nome:')
 try:
        idade = int(input('Idade: '))
 except ValueError:
        print('Digite um número inteiro')
        idade = int(input('Idade: '))
 salario = float(input('Salário: '))
 sexo =  input('Sexo: ')
 estadoCivil =  input('Estado Civil: Solteiro[s] | Casado[c] | Viúvo[v]| Divorcidado[d] ')

 if len(nome)>3 and idade>0 and idade<150 and salario>0:
     if salario>0:
          if sexo=='f' or sexo=='m':
               if estadoCivil=='s' or estadoCivil=='c' or estadoCivil=='v' or estadoCivil=='d':
                    print('Cadastro feito com sucesso')
                    break;
 else:
       print('Cadastro inválido.Tente novamente')     
      
       