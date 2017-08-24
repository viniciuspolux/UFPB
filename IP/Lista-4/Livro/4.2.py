#4.2

velocidade = float(input('Digite sua velocidade :'))

if velocidade > 80 :
    print('Você foi multado')
    multa1 = (velocidade - 80)*5
    print('Você terá que pagar {:.2f} reais'.format(multa1))
else :
    print('Você não foi multado!')
    
