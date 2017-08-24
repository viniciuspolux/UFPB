pedido,quantidade = map(int, input("Digite seu pedido e a quantidade = ").split())

if (pedido==1):
    res= (quantidade*4.00)

elif(pedido==2):
    res= (quantidade*4.50)

elif(pedido==3):
    res= (quantidade*5.00)

elif(pedido==4):
    res= (quantidade*2.00)

elif(pedido==5):
    res= (quantidade*1.50)

print("Total: R$ {:.2f}" .format(res))
