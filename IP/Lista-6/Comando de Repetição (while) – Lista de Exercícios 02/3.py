cont=50
res=0

while (cont > 0):
    numero=(int(input("Digite um número: ")))
    
    if numero % 3 == 0:
        res+= numero
        cont -= 1
    else:
        cont -= 1

print(res)
