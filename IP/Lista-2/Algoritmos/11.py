valor=(int)(input("Digite o valor do veículo: "))
distribuidor= 28
imposto= 45

res=((imposto/100 * valor) + (distribuidor/100 * valor) + valor)

print("O valor final do veículo é R$ {} " .format(res))
