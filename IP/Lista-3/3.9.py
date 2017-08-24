salario = int(input("Digite seu salario atual: "))
aumento = int(input("Digite a porcentagem do aumento: "))
salariototal = (salario + (salario * aumento / 100))
aumento2 = (salario * aumento / 100)

print("O valor do aumento é R$:", aumento2)
print("O salario total é R$:", salariototal)
