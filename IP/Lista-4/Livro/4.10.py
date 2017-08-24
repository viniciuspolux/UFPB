# 4.10

energia = float(input('Digite a quantidade de KWh :'))
tipo = input('Digite (R) para residência, (I) para industria e (C) para comercio : ')

if tipo == 'r' :
    if energia <= 500:
        energia1 = energia*0.40
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))
    else :
        energia1 = energia*0.65
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))
if tipo == 'c':
    if energia <= 5000:
        energia1 = energia*0.55
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))
    else :
        energia1 = energia*0.60
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))
if tipo == 'i':
    if energia <= 1000:
        energia1 = energia*0.55
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))
    else :
        energia1 = energia*0.60
        print ('O valor da energia a ser pago é : {:.2f}'.format(energia1))

    
