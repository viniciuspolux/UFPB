numeroa=(int(input("Digite o primeiro número: ")))
numerob=(int(input("Digite o segundo número: ")))
cont=0

if numeroa>numerob:
    numeroa,numerob=numerob,numeroa

for i in range(numeroa,numerob):
    if i % 4 == 0:
        cont+=1
print("{} múltiplos" .format(cont))
