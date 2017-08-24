dias = 6340

anos = (int)(dias / 365)
meses = (int)((dias % 365) /30)
dias = (int)((dias % 365) % 30)


print("São {} ano(s), \n{} mese(s) e \n{} dia(s)." .format(anos,meses,dias))
