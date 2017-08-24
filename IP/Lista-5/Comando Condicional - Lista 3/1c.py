#O programa deve receber como entrada três números inteiros e exibir
#qual o maior deles. (Dica: desconsidere a possibilidade de números iguais
#na entrada)

#Não é necessaŕio o uso de 3 if. Um if e dois elif são suficiente.

a=int(input("Digite um número = "))
b=int(input("Digite um número = "))
c=int(input("Digite um número = "))

if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
elif (c>a) and (c>b):
    print(c)
