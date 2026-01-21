def factorial (numero):
    calculo = 1
    cont = 1

    while cont < numero:
        if cont+1 <= numero:
            calculo = calculo * (cont+1)
        print(calculo)
        cont += 1

    return calculo

numero = 5
print(factorial(numero))