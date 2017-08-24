valorsegundos = 4653

horas = (int)(valorsegundos / 3600)
minutos = (int)((valorsegundos % 3600)/60)
segundos = ((valorsegundos % 3600) % 60)

print("{} hora(s), \n{} minuto(s), \n{} segundo(s)." .format(horas,minutos,segundos))
