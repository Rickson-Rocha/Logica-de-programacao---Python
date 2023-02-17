import os
os.system('cls')


class EnumChoice:
    CADASTRAR = 'c'
    PESQUISAR ='p'
    SAIR ='s'
    EXCLUIR = 'x'
    EDITAR = 'e'

#Funções cuja responsabilidade é verificar e validar informações passadas pelo usuário

def entra_int():
    while True:
        try:
         entrada = int(input('Idade: '))
        except:
            print('Idade inválida')
        else:
            return entrada

#validando cpf->(tamanho da string):

def entrada_cpf():
    while True:
        cpf = input('CPF: ')
        if len(cpf)==11 and cpf.isnumeric():
            cpf = cpf
            break;
        else:
            print('CPF INVÁLIDO. TENTE NOVAMENTE')

def entra_fone():
   while True:
        fone = input('FONE:(DD): ')
        if len(fone)==11 and fone.isnumeric():
            fone = fone
            break;
        else:
            print('Telefone INVÁLIDO. TENTE NOVAMENTE')


contatos = {}
#cpf,nome,idade,telefone
placeholder = ''
while True:
    op = input('Escolha uma opção: Cadastrar[c] | Editar[e] | Pesquisar[p] | Excluir[x]  | Sair[s]: ').lower()

    match(op):
        case  EnumChoice.CADASTRAR:
          cpf= entrada_cpf()
          nome = input('Nome: ').lower()
          idade = entra_int()
          tel = entra_fone()

          contatos[cpf] = {
              'cpf': cpf,
              'nome': nome,
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
                    idade = entra_int()
                    cpf = entrada_cpf()
                    tel = input('Fone: ')

                    contatos[busca] = {
                        'cpf': cpf,
                        'nome': nome,
                        'idade':idade,
                        'tel':tel
                    }
                    print('Contato editado.')

                except KeyError:
                    print('Chave inválida.Tente novamente')
                else:
                    break

        case EnumChoice.EXCLUIR:
              while True:
                busca = input('Insira o cpf do contato o qual deseja excluir : ')
                try : 
                 contatos[busca].pop
                except:
                    print('CPF inválido.Tente novamente')
                    
        case  EnumChoice.SAIR:
            print('Programa encerrado.')
            break
print(contatos)