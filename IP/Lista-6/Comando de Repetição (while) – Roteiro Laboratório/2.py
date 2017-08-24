numeroa,numerob=map(int,input("Digite dois números com um espaço entre eles =").split())

x=1
while x < 2 :
    soma= numeroa + numerob
    prod= numeroa * numerob
    x += 1
print("{} {}" .format(soma,prod))
