dias = int(input("Digite quantos dias o carro ficou alugado: "))
km = int(input("Digite quantos KM o carro percorreu: "))

res = dias * 60
kmrodado = km * 0.15
dia = 60

if(dias > 1):

    valor = (res + kmrodado)
    print("Você vai pagar: ", res)

else:
    valorb = (dia + kmrodado)
    print("Você vai pagar: ", valorb)
