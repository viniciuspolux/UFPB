numeroa,numerob=map(int,input("Digite dois números com um espaço entre eles =").split())

x=1
while x < 2 :
    if(numeroa > 0 and numerob > 0):
        soma= numeroa + numerob
        prod= numeroa * numerob
        print("{} {}" .format(soma,prod))
    else:
        print("Você digitou um número inválido")
    x += 1
