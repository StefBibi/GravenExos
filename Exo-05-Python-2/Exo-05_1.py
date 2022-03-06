# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # afficher 'bienvenue au ciné'
    print("Bienvenue au cinéma")

    # Liste des films
    film_list = ["Voyage au centre de la terre", "Retour vers le futur", "Algobox - le film"]

    # les afficher
    """cpt = 0
    for film in film_list:
        cpt += 1
        print("Film n°" + str(cpt) + " : " + film)"""
    for numero, film in enumerate(film_list, start=1):
        print("Film n°", numero, ":", film)
