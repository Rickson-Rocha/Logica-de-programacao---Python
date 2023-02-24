#Faça um programa que peça dois números, base e expoente, 
#calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("base: "))
expoente = int(input("expoente: "))
mult = 1

for i in range(expoente):
    if expoente==0:
        calc2 = 1
    else:
        calc1 =  base*base 
        calc2 = base * calc1
print(calc2)