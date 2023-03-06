#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#Apresentando três de formas de resolução para o mesmo problema:

def soma(a,b,c):
    return a+b+c
print(soma(1,2,3))

somaLam  = lambda a,b,c: a+b+c
print(somaLam(1,2,3))

def somaArgs(*args):
    return sum(args)
print(somaArgs(1,2,3))