salario = float(input('Digite seu salário:'))

if salario >= 1000 :
    imposto = salario*(17/100)
    print('O valor do imposto a ser pago será igual a {:.3f} reias'.format(imposto))

else :
    imposto = salario*(8/100)
    print('O valor do imposto a ser pago será igual a {:.3f} reais'.format(imposto))
    
