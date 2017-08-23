numeroa=(int(input("Digite o primeiro valor = ")))
numerob=(int(input("Digite o segundo valor =")))

cont=0
r=numeroa

while numerob <= r:
    if numeroa == 0 or numerob == 0 :
        print("Não será possível a divisão")
        break

    else:
        if (numerob > r):
            print("O resultado da divisão é {} e o resto {}".format(cont,r))
            
        else:
            r -= numerob
            cont += 1

print("O resultado da divisão é {} e o resto {}" .format(cont,r))
