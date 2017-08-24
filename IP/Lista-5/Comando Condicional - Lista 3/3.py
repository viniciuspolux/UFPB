quantidade=(int(input("Digite a quantidade de pessoas = ")))

onibus= 42
van= 20
precobus= 350
precovan= 200

if(quantidade <= 41 ):
 
    if(quantidade <= 20):
        lotvan= 1
        lotbus= 0

    else:
        lotvan= 2
        lotbus= 0

    valorvan= lotvan * precovan
    valorbus= 0
    pgvan= valorvan / quantidade
    pgbus= 0

else :
    
    if(quantidade == 42):
        lotbus= 1
        lotvan= 0

    elif(quantidade <= 52):
        lotbus= quantidade // onibus
        lotvan= 1
        
    else:
        lotbus= quantidade // onibus
        lotvan= round(((quantidade % onibus)/van))

    valorvan= lotvan * precovan
    valorbus= lotbus * precobus
    
pgvan= valorvan / quantidade
pgbus= valorbus / quantidade 
valorfinal= pgvan + pgbus         

print("{} ônibus e {} van(s)\nR$ {:.2f} por pessoa." .format(lotbus,lotvan,valorfinal))
