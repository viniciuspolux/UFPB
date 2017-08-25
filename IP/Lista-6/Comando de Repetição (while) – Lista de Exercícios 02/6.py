quantidade= int(input("Digite a quantidade de filhos: "))
cont=0
res=0

while (quantidade > 0):
    res += quantidade
    cont += 1
    media= res // cont
    quantidade= int(input("Digite a quantidade de filhos: "))
print("A média de filhos é de {}" .format(media))
