# 4.9

casa = float(input('Digite o valor da casa que você quer comprar em real :'))
salario = float(input('Digite o valor do seu salário em real :'))
anos = int(input('Pretende pagar em quantos anos :'))
meses = anos*12
prestacao = casa/meses

if prestacao < (salario-(salario*0.7)):
    print ('Voce podera pagar: {:.2f} reais, por mês'.format(prestacao))
else :
    print ('O valor da prestação é igual a : {:.2f}'.format(prestacao))
    print ('O valor da prestação não pode ser maior que 30% do seu salário!')
