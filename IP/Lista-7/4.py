quant=int(input("Quantidade de produtos: "))
deco,eletro = 0,0
movel,valor = 0,0
marcaa, marcab = 0, 0
marfim, branco = 0,0
percentual,percentualb=0,0

for i in range(quant) :

    tipo=str.lower(input("Tipo de Produto: "))

    if tipo == "movel" or tipo == "móvel":
        cor= str.lower(input("Cor: "))
        movel+=1

        if cor == "marfim":
            marfim += 1
        elif cor == "branco":
            branco += 1
        
    elif tipo == "eletrodoméstico" or tipo == "eletrodomestico":
        marca=str.lower(input("Marca: "))
        eletro+=1

        if marca == "electrolux":
            marcaa += 1
        else:
            marcab +=1

    elif tipo == "decoração" or tipo == "decoraçao":
        deco += 1
        preco=int(input("Preço: R$ "))
        valor+= preco
        media= valor/deco

if marfim > 0 and marfim == branco:
    total= marfim + branco
    percentual= 100 // total
    percentualb= percentual

elif marfim == 0 and branco != 0:
    percentual= 0
    percentualb= 100//branco

elif marfim != 0 and branco == 0:
    percentual= 100 // marfim
    percentualb=0

elif marfim != branco:
    percentual= 100 // marfim
    percentualb= 100 // branco

print("Percentuais: {:.0f}% marfim, {:.0f}% branco." .format(percentual,percentualb))

if movel == 0:
    print("Nenhum móvel vendido")

if eletro > 0:
    if marcaa > marcab:
        print("Marca mais vendida: Electrolux")
    elif marcaa < marcab:
        print("Marca mais vendida: Brastemp")
    elif marcaa == marcab:
        print("As duas marcas foram igualmente vendidas")
    
elif eletro == 0:    
    print("Nenhum eletrodoméstico vendido")

if deco > 0:
    print("Preço médio de Decoração: R$ {:.0f}" .format(media))

elif deco == 0:
    print("Nenhum objeto de decoração vendido")
        
