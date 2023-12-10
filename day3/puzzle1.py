with open('input.txt', 'r') as file:
    lines = file.readlines()

matriz = []
for line in lines:
    row = line.strip()
    matriz.append(row)

suma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        ##########################################################################
        if matriz[i][j].isdigit():
            # Comprobar los vecinos (incluyendo diagonales)
            esContable = False
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0 <= i + x < len(matriz) and 0 <= j + y < len(matriz[i]):
                        # Verificar si el vecino no es un dígito
                        if not matriz[i + x][j + y].isdigit():
                            esContable = True
                            break  # Romper el bucle una vez se encuentra un vecino no numérico
                if esContable:
                    break

            if esContable:
                suma += int(matriz[i][j])

print(f"La suma de los números requeridos es: {suma}")
