idade=int(input("Digite a idade: "))
res=0

while (idade >= 3 and idade <= 6):

    res += 1
    duvida= str.lower(input("Deseja Continuar: "))

    if(duvida == "sim" or duvida == "s"):
        idade=int(input("Digite a idade: "))
    else:
        break
        
print("Foram aplicadas {} vacinas" .format(res))
