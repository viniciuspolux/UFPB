quant=int(input("Digite a quantidade de lavagens: "))
res=0
cont=0
total=0

for i in range(quant):

    tipocobra=str.lower(input("Digite o tipo de cobrança: "))
     
    if tipocobra == "peça":
        quant=int(input("Digite a quantidade de peças: "))
        lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
        cont = quant * 7 

        if lavagem == "s":    
            res = 1
            cont += 3.5
        print("Valor do pedido: R$ {:.2f} " .format(cont))

    elif tipocobra == "peso":
        quilos= int(input("Digite a quantidade de quilos: "))
        lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
        cont= quilos * 5

        if lavagem == "s":    
            res = 1
            cont += 3.5
        print("Valor do pedido: R$ {:.2f} " .format(cont))
    total+=cont

print("Total arrecadado: R$ {} " .format(total))
print("Quantidade de lavagens a seco: {} " .format(res))
