numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite outro numero: "))
if numero1 > numero2 and numero1 > numero3:
    print("O maior numero é: ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior numero é: ", numero2)
else:
    print("O maior numero é: ", numero3)
    
