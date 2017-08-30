ruim,regular=0,0
bom,excelente=0,0
acima30,cont=0,0
temp=0
for i in range(6):

    idade=int(input("Idade: "))
    qualidade=str.lower(input("Classificação: "))

    if qualidade == "ruim":
        ruim +=1

    elif qualidade == "regular":
        regular += 1

    elif qualidade == "bom":
        cont += idade
        bom += 1

    elif qualidade == "excelente":
        if idade > 30:
            acima30 += 1

    if idade > temp:
        maior=idade 
        temp=maior

quant= ruim+regular
media= cont // bom

print("Média de idade Bom: {}" .format(media))
print("Quantidade respostas Ruim/Regular: {}" .format(quant))
print("Pessoas acima de 30 Execelente: {}" .format(acima30))
print("Maior idade: {}" .format(temp))
