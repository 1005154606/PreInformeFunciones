def primo(n):
    contador = 0
    for x in range(1, n + 1):
        if n%x == 0:
            contador= contador+ 1

    if contador<=2:
        print("el número es primo ")
    else:
        print("el número no es primo ")


n = int(input("ingrese el número: "))
primo(n)






