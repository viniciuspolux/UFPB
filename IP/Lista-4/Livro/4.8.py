# 4.8

num1 = float(input('Digite o primeiro número :'))
num2 = float(input('Digite o segundo número :'))
ope = input('Digite (+) para somar, (-) para subtrair, (*) para multiplicar e (/) para dividir : ')

if ope == '+' :
    soma = num1+num2
    print(soma)
elif ope == '-':
    subt = num1-num2
    print(subt)
elif ope == '*' :
    mult = num1*num2
    print(mult)
elif ope == '/' :
    div = num1/num2
    print(div)
else :
    print('Condição invalida')
