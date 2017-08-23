from random import choice

afazeres = ["Varrer", "Lavar os pratos", "lavar o vaso", "limpar o banheiro"]

nome = str.capitalize(input("Type your name: "))

if (nome == "Dadinho" or nome == "Ronaldo"):
    print("%s será responsável por dar a bunda" % (nome))
else:
    print("%s será responsável por %s" % (nome, choice(afazeres)))