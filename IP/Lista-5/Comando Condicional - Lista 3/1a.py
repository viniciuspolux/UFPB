#O programa deve receber como entrada a renda anual de uma pessoa e exibir o
#imposto total a ser pago. Quem ganha até 12000 fica isento, quem ganha mais de
#60000 paga 7% desse valor, e os demais pagam 3% do valor total.

#  No Programa original ele usou dois if, ao invés do segundo
# usaria o elif para evitar processamentos desnecessários.

rendaAnual=float(input("Digite sua Renda Anual = "))

if (rendaAnual <= 12000):
    imposto=0
elif(rendaAnual > 60000):
    imposto=rendaAnual*0.07
else:
    imposto=rendaAnual*0.03
print(imposto)
