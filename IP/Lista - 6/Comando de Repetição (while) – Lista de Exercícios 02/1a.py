# Programa para ler 20 números e exibir a soma dos pares.

cont = 20
soma=0
while (cont > 0):
    numero = int(input())
    if (numero % 2 == 0):
        soma += numero 
    cont -= 1
print(soma)

#O programa não executava porque a condição do while está invertida, logo
#ele entraria em um loop infinito, e o mesmo não estava somando,
#apenas atribuando o valor de numero a soma.
