combustivel=(str.lower(input("Qual combustível de preferência = ")))
valor=(float(input("Digite o valor em dinheiro que deseja gastar = R$ ")))

if(combustivel == "gasolina"):
    valorfinal = valor/2.53
    print("Não Ganhou troca de óleo !")

elif(combustivel == "etanol"):
    valorfinal = valor/2.09
    
    if(valorfinal >= 30):
        print("Ganhou troca de óleo !")
    else:
        print("Não Ganhou troca de óleo !")

elif(combustivel == "diesel"):
    valorfinal = valor/1.92
    print("Não Ganhou troca de óleo !")

print("{:.2f} litros" .format(valorfinal))
