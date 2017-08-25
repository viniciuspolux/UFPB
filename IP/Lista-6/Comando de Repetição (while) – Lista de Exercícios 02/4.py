numero=int(input())
cont=0
res=0

while numero != 100:

    if numero % 2 == 0:
        cont += 1
        res += numero

    numero=int(input())

if cont > 0:
    print(res // cont)

else:
    print("Não foram lidos números pares")
    
