import math

print("------- Calcolatrice personale ------- \n")

print("Quale perimetro vuoi calcolare? \n")

while True:
    try:
        scelta = int(input("1) Quadrato\n2) Cerchio\n3) Rettangolo\n4) Esci \n"))

        if 1 <= scelta <= 4:
            break
        else:
            print("Scelta invalida, prova un altro numero. \n")

    except ValueError:
            print("Scelta invalida, per favore inserire un numero. \n")

if (scelta == 1):

    lato = 0 

    while lato == 0:
        lato = int(input("Inserire un lato del quadrato da inserire: \n"))
        if lato == 0:
            print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero. \n")

    perimetro = lato * 4

    print("Il perimetro del quadrato inserito è: ", perimetro)

elif (scelta == 2):

    raggio = 0 

    while raggio == 0:
        raggio = int(input("Inserire il raggio del cerchio da inserire: \n"))
        if raggio == 0:
            print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero. \n")

    perimetro = 2 * math.pi * raggio

    print("Il perimetro del cerchio inserito è", perimetro)

elif (scelta ==3 ):


    base = 0 

    while base == 0:
        base = int(input("Inserire la base del rettangolo da inserire: \n"))
        if base == 0:
            print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero. \n")

    altezza = 0

    while altezza == 0:
        altezza = int(input("Inserire l'altezza del rettangolo da inserire: \n"))
        if altezza == 0:
            print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero. \n")

    base = base * 2

    altezza = altezza * 2

    perimetro = base + altezza

    print("Il perimetro del rettangolo inserito è: ", perimetro)

elif (scelta == 4):

    print("Arrivederci!")

