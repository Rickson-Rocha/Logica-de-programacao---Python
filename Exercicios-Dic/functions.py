#Funções cuja responsabilidade é verificar e validar informações passadas por usuário


def entra_int():
    while True:
        try:
         entrada = int(input('Idade: '))
        except:
            print('Idade inválida')
        else:
            return entrada

#validando cpf->:

def entrada_cpf():
    while True:
        cpf = input('CPF: ')
        if len(cpf)==11 and cpf.isnumeric():
           return cpf
        else:
            print('CPF INVÁLIDO. TENTE NOVAMENTE')

def entra_fone():
   while True:
        fone = input('FONE:(DD): ')
        if len(fone)==11 and fone.isnumeric():
          return fone
        else:
            print('Telefone INVÁLIDO. TENTE NOVAMENTE')

def imprime_contatos(contatos, chaves):
  table = []
  for chave in chaves:
    table.append([
      contatos[chave]["nome"],
      contatos[chave]["telefone"],
      contatos[chave]["email"]
    ])
  return table