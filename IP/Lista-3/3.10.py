preco = int(input("Digite o preco do produto: "))
desconto = int(input("Digite a porcentagem do desconto: "))
precototal = (preco - (preco * desconto / 100))
desconto2 = (preco * desconto / 100)

print("O desconto é no valor de R$:", desconto2)
print("O valor com desconto é R$:", precototal)
