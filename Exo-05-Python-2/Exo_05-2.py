# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # afficher 'bienvenue au ciné'
    print("Bienvenue au cinéma")

    # Liste de dictionnaire des films
    films_list = [
        {  # film 1
            'titre': "Voyage au centre de la terre",
            'horaire': "17h00",
            'places': 200
        },
        {  # film 2
            'titre': "Les 9 jsons cachés",
            'horaire': "18h00",
            'places': 80
        },
        {  # film 2
            'titre': "Algobox - Le Film",
            'horaire': "19h00",
            'places': 2
        }
    ]

    for numero, film in enumerate(films_list, start=1):
        titre = film['titre']
        heure = film['horaire']
        places = film['places']
        #print("Film n° {} : {}, heure : {}, places dispo : {}".format(numero, titre, heure, places))
        print(f"Film n° {numero} : {titre}, heure : {heure}, places dispo : {places}")
