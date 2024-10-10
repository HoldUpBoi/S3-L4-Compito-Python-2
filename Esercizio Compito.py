
print("--- Programma calcolo perimetro rettangolo ---\n \n")

base = 0 

while base == 0:
    base = int(input("Inserire la base del rettangolo da inserire: \n"))
    if base == 0:
        print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero.")

altezza = 0

while altezza == 0:
    altezza = int(input("Inserire l'altezza del rettangolo da inserire: \n"))
    if altezza == 0:
        print("Il numero inserito è zero. Per favore, inserisci un numero diverso da zero.")

base = base * 2

altezza = altezza * 2

perimetro = base + altezza

print("Il perimetro del rettangolo inserito è: ", perimetro)

