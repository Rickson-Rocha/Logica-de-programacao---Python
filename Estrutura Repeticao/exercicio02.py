# Faça um programa que leia um nome de usuário e a sua senha 
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

#Nesse caso existirá diferenciação entre letras maiúsiculas e minúsculas -> ademir # Ademir
#Caso deseje que os valores sejam diferentes,basta fazer conversão dos valores  para lower() e depois prosseguir com a comparação
while True:
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    if usuario!=senha:
        print('Acesso concedido')
        break
    else:
        print('Nome de senha e usuários devem ser diferentes')