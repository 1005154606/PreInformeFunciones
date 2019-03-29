def num_herm(num):
    n=num+1
    contador=0
    for i in range(1,n+1):
        if n%i==0:
            con=contador+1
    if con <=2 and num%6 != 0:
        print("el número es primo hermano")
    else:
        print("el número no es primo hermano")


num=int(input("ingrese el número"))
num_herm(num)