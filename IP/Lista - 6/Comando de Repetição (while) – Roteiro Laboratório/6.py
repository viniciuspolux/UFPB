numeroa,numerob=map(int,input("Digite dois números com um espaço entre eles =").split())
x=1

while x == 1  :

    if(numeroa > 0 and numerob > 0):
        soma= numeroa + numerob
        prod= numeroa * numerob
        print("{} {}" .format(soma,prod))

    else:
        media= (numeroa + numerob) // 2
        print("{}" .format(media))

    decisao= (str.lower(input("Deseja realizar uma nova execução = ")))

    if(decisao == "sim"): 

        numeroa,numerob=map(int,input("Digite dois números com um espaço entre eles =").split())

    else:

        break
