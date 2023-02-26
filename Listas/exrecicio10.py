#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
v1 = []
v2 = []
v3 = []

for i in range(5):
    nV1 = int(input(f'{i+1}º: '))
    v1.append(nV1)

for i in range(5):
    nV2 =  int(input(f'{i+1}º: '))
    v2.append(nV2)

for i in range(len(v1)):
     v3.append(v1[i])
     v3.append(v2[i])

print(v1)
print(v2)
print(v3)