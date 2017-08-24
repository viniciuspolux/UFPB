# 4.6

distancia = float(input('Digite a distancia que você quer percorrer em Km :'))

if distancia <= 200 :
    passagem = (distancia*0.5)
else :
    passagem = (distancia*0.45)

print('O preço da passagem : {} reais'.format(passagem))
