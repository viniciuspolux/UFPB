# Programa para ler 30 números e exibir a quantidade de positivos

cont = 30
qtdePositivos = 0

while (cont > 0):
    numero = int (input())

    if (numero >= 1):
        res = numero//numero
        qtdePositivos += res
        cont -= 1
    else:
        cont -= 1

print(qtdePositivos)

#O programa original estava com alguns problemas, um deles seria que esta pedindo
#o valor ao usuário antes do while e isso faz com que o usuario so possa digitar
#uma unica vez, a condição do while estava errada pois estava dizendo que quando
#cont for maior que, mas o valor de cont é 0 e o programa não irá rodar, e se ele
#entrasse no while a variavel qtdePositivos estava recebendo o valor do numero e
#somando 1, fazendo com que no final não seja o valor de quantos numeros são
#positivos e por ultimo temos que colocar um else caso o numero for menor que 0.
