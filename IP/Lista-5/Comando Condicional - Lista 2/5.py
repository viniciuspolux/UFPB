valor=(float(input("Valor do produto = ")))
formadepg=(str.lower(input("Forma de Pagamento = ")))

if (valor >= 100):

    if(formadepg == "dinheiro" ):
        desconto = (10/100)
        valorfinal = (valor - (desconto * valor))
        print("R$ {}" .format(valorfinal))

    elif(formadepg == "cheque"):
        print("R$ {}" .format(valor))

    else:
        print(" ({}) Forma de pagamento inválida" .format(formadepg))

elif (valor < 100):

    if (formadepg == "dinheiro"):
        print("R$ {}" .format(valor))

    elif (formadepg == "cheque"):
        print("R$ {}" .format(valor))

    else:
        print(" ({}) Forma de pagamento inválida" .format(formadepg))
