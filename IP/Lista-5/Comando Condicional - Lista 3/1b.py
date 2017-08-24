#O programa deve receber como entrada a altura de uma pessoa e exibir uma
#mensagem informando se ela é de estatura baixa, mediana ou alta.

#O código possui um erro no qual o if e o else estão dentro de um else
#quando na verdade era necessaŕio apenas colocar um elif.

altura=float(input("Digite sua Altura = "))

if(altura <= 1.40):
    print("Estatura Baixa")
elif(altura < 1.65):
    print("Estatura Mediana")
else:
    print("Estatura Alta")
