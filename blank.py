equipos_de_futbol = {'1': "Junior",
                     '2': "America",
                     '3': "Cali",
                     '4': "Union Magdalena",
                     '5': "Pasto"}
equipos_de_la_nba = ["Heat", "Blazers", "Timberwolves", "Lakers", "Spurs", "Rokets"]
print(equipos_de_futbol)
print(equipos_de_la_nba)
equipos_de_la_nba.sort()
print(equipos_de_la_nba)

while True:
    choice = input("What is the best team in Colombian futbol?")


    if choice == 0:
        break

    if choice == 'Junior':
        print("Acertaste! JUNIOR TU PAPA, LO DEMAS VALE ...")
        break

    else:
        print("Elige otro equipo")


