cf = int(input("Cigarros fumados por dia: "))
af = int(input("Anos como fumante: "))
tc = (af * 365) * cf
dp =(tc * 10) / 24
print('Dias perdidos %d'%dp)
