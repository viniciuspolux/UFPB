m=(int(input("Digite o valor de M: ")))
n=(int(input("Digite o valor de N: ")))

if n<m :
    x=m
    m=n
    n=x
    
    
while m <= n:
    print (m)
    m += 1
