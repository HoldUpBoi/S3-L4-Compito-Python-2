checkstring = input("Inserire frase da contare: \n")

wordcount = len(checkstring.split())
lettercount = len([char for char in checkstring if char.isalpha()])
spacescount = len([char for char in checkstring if char.isspace()])

print("Ci sono ", wordcount, " parole, ", lettercount, " lettere e ", spacescount, " spazi in questa frase.")