valor=(float(input("Valor do produto = ")))
formadepg=(str.lower(input("Forma de Pagamento = ")))

if(formadepg == "cartao"):
    funcaocartao=(str.lower(input("Função = ")))
                  
    if(funcaocartao == "credito"):
        parcela=(int(input("Parcelas = ")))


if(valor >= 100):

    if(formadepg == "dinheiro" ):
        valorfinal= (valor - (valor * 0.10))
        print("R$ {}" .format(valorfinal))

    elif(formadepg == "cheque"):
        print("R$ {}" .format(valor))

    elif(formadepg == "cartao"):

        if (funcaocartao == "debito"):
            print("R$ {} " .format(valor))

        elif(funcaocartao == "credito"):

            if(parcela <= 3):
                valorfinal= valor / parcela
                print("R$ {} \n {} parcela(s) de {:.2f} " .format(valor,parcela,valorfinal))

            else:
                print("Quantidade de parcelas inválidas")

elif(valor < 100):

    if (formadepg == "dinheiro"):
        print("R$ {}" .format(valor))

    elif (formadepg == "cheque"):
        print("R$ {}" .format(valor))

    elif (formadepg == "cartao"):

        if (funcaocartao == "debito"):
            print("R$ {} " .format(valor))

        elif(funcaocartao == "credito"):

            if(parcela <= 3):
                valorfinal= valor / parcela
                print("R$ {} \n {} parcela(s) de {} " .format(valor,parcela,valorfinal))

            else:
                print("Quantidade de parcelas inválidas")
