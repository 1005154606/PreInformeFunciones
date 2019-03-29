acum1=0
acum2=0
def potencia(a, b):
    c = a ** b
    print(c)
    return c
for x in range(0,2):
    a = int(input("Introduce la base :"))
    b = int(input("Introduce el exponente :"))
    if x==0:
        acum1=acum1+potencia(a,b)
    else:
        if x==1:
            acum2=acum2+potencia(a, b)
if acum1==acum2:
    print(acum1,"es igual que ",acum2)
if acum1>acum2:
    print(acum1,"es mayor que ",acum2)
else:
    acum1, "es mamenor que ", acum2








