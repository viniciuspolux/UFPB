d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))
segtotal = (d * 86400) + (h * 3600) + (m * 60) + s

print("O total de segundos é", segtotal)
