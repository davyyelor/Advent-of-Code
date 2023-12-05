import csv 

with open("input.txt") as f:
    reader = csv.reader(f)
    data = list(reader)


    games_divided = []

    for game in data:
        game_data = ' '.join(game) 
        game_data = game_data.split(': ')  
        game_id = game_data[0]  
        cube_data = game_data[1].split('; ')  
        
        game_info = [game_id]
        for cube_info in cube_data:
            cubes = cube_info.split(' ')
            for cube in cubes:
                game_info.append(cube)
        games_divided.append(game_info)

suma = 0
for game_info in games_divided:
    i = 0
    print(game_info)  

    cubosRojos = 0
    cubosAzules = 0
    cubosVerdes = 0
    Fin = False
    while i < len(game_info) and not Fin:
        if game_info[i].isdigit():
            print ("Cubo", game_info[i])

        if game_info[i] == "blue":
            print ("Color", game_info[i])
            cubosAzules = int(game_info[i-1])

        if game_info[i] == "red":
            print ("Color", game_info[i])
            cubosRojos = int(game_info[i-1])

        if game_info[i] == "green":
            print ("Color", game_info[i])
            cubosVerdes = int(game_info[i-1])

        if "Game" in game_info[i]:
            print ("Juego", game_info[i])

            juegos = game_info[i].split(" ")
            id = int(juegos[1])
            print("Id: ", id)

        if cubosAzules > 14 or cubosRojos > 12 or cubosVerdes > 13: 
            print ("No se puede jugar: Azules, Rojos, Verdes", cubosAzules, cubosRojos, cubosVerdes)
            Fin = True

        i += 1
    
    if Fin == False:
        print("Se va a incluir el valor del juego", id, "Cubos azules:", cubosAzules, "Cubos rojos:", cubosRojos, "Cubos verdes:", cubosVerdes)
        suma += id

print("El valor final es:", suma)

