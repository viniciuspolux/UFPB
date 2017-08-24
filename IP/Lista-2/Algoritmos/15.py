valor=int(input("Digite o valor = "))

cem=(valor // 100)
dinheiro= (valor % 100)

cinquenta=(dinheiro // 50)
dinheiro= (dinheiro % 50)

vinte=(dinheiro // 20)
dinheiro=(dinheiro % 20)

dez= (dinheiro // 10)
dinheiro= (dinheiro % 10)

cinco= (dinheiro // 5)
dinheiro= (dinheiro % 5)

dois= (dinheiro // 2)
dinheiro= (dinheiro % 2)

um= (dinheiro)

print("{} \n{} nota (s) de R$ 100,00 \n{} nota (s) de R$ 50,00 \n{} nota (s) de R$ 20,00  \n{} nota (s) de R$ 10,00 \n{} nota (s) de R$ 5,00  \n{} nota (s) de R$ 2,00 \n{} nota (s) de R$ 1,00 " .format (valor,cem,cinquenta,vinte,dez,cinco,dois,um))
