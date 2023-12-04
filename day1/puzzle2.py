import csv

with open("input.txt") as f:
    reader = csv.reader(f)
    data = list(reader)


    processed_data = []
    for line in data:
        processed_line = ""
        for word in line:
            word = (
                word.replace("one", "one1one")
                .replace("two", "two2two")
                .replace("three", "three3three")
                .replace("four", "four4four")
                .replace("five", "five5five")
                .replace("six", "six6six")
                .replace("seven", "seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine", "nine9nine")
            )
            processed_line += word
        processed_data.append([processed_line])

    valor = 0
    for line in processed_data:
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
