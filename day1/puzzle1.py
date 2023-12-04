import csv

with open("input.txt") as f:
    reader = csv.reader(f)
    data = list(reader)

    valor = 0
    for line in data:
        cadena = ""
        primera = ""
        ultima = ""
        for palabras in line:
            for char in palabras:
                if char.isdigit():
                    if primera == "":
                        primera = char
                    ultima = char
            if primera != "":
                cadena += primera + ultima
                primera = ""
                ultima = ""

        if cadena != "":
            valor += int(cadena)

    print("El valor final es:", valor)
