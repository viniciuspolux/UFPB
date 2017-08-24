# 4.4

salario = float(input('Digite o valor do salário:'))

if salario >= 1250 :
    salario = salario*0.10
else :
    salario = salario*0.15

print('O valor do aumento em seu salário é igual a : {}'.format(salario))
