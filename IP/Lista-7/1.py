quant=int(input("Digite a quantidade de produtos: "))
cont=0
valorfinal=0
maior=0

for i in range(quant):

    descricao=(input("Descrição do produto: "))
    valor=int(input("Digite o valor do produto: "))
    ano=int(input("Digite o ano do produto: "))

    if ano < 1827:
        cont += 1

    if valor > maior:

        maior = valor
        anob= ano
        descricaob=descricao

    valorfinal += valor

preco = valorfinal / quant
print("Itens produzidos antes de 1827 : {}" .format(cont))
print("Valor médio dos itens : {:.2f}" .format(preco))
print("Dados do objeto mais valioso : {},{}" .format(descricaob,anob))
