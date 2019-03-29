def imp(a):
    a%2
    if a%2!=0:
        print(a)

n=int(input("Introduce un número: "))
for x in range(1, n+1):
    imp(x)