import os

import tabulate

os.system('cls')
from functions import*


class EnumChoice:
    CADASTRAR = 'c'
    PESQUISAR ='p'
    SAIR ='s'
    EXCLUIR = 'x'
    EDITAR = 'e'



 
contatos = {}
#cpf,nome,idade,telefone
placeholder = ''
while True:
    op = input('Escolha uma opção: Cadastrar[c] | Editar[e] | Pesquisar[p] | Excluir[x]  | Sair[s]: ').lower()

    match(op):
        case  EnumChoice.CADASTRAR:
          nome = input('Nome: ').lower()
          cpf= entrada_cpf()
          idade = entra_int()
          tel = entra_fone()

          contatos[nome] = {
              'nome': cpf,
              'cpf': cpf,
              'idade':idade,
              'tel':tel
          }

        case  EnumChoice.PESQUISAR:
            while True:
                busca = input('Encontre: ')

                try : print(contatos[busca])
                except KeyError:
                    print('Chave inválida.Tente novamente')
                else:
                    break

        case EnumChoice.EDITAR:
             while True:
                busca = input('Insira o cpf do contato o qual deseja alterar : ')

                try : 
                    nome = input('Nome: ').lower()
                    cpf= entrada_cpf()
                    idade = entra_int()
                    tel = entra_fone()

                    contatos[nome] = {
                        'nome': cpf,
                        'cpf': cpf,
                        'idade':idade,
                        'tel':tel
                    }

                except KeyError:
                    print('Chave inválida.Tente novamente')
                else:
                    break

        case EnumChoice.EXCLUIR:
              while True:
                busca = input('Insira o cpf do contato o qual deseja excluir : ')
                try : 
                 contatos[busca].pop
                except KeyError:
                    print('CPF inválido.Tente novamente')
                    
        case  EnumChoice.SAIR:
            print('Programa encerrado.')
            break

print(tabulate(table, headers=["nome", "cpf", "idade","tel"], tablefmt="grid"))