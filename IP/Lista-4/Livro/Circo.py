idade = int(input('Digite sua idade :'))

if idade <= 5 :
    valor = 10
elif idade >= 60 :
    valor = 15  
else :
    valor = 25
    
print('Você pagara {} reais'.format(valor))
