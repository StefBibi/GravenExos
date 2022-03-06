from tkinter import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fenetre = Tk()

    fenetre.title("Cinema systeme de reservation")
    fenetre.geometry("400x300")

    # fonction du bouton 'Reserver'
    def click_button(film_id, new_place):
        print("OK :", film_id)
        choix = film_id - 1
        if choix not in range(3):
            print("mauvais choix")
        else:
            print("vous avez choisit le film :", films_list[choix]['titre'])
            nb_places = films_list[choix]['places']
            if nb_places > 0:
                print("Reservation effectuee !")
                films_list[choix]['places'] -= 1
                print(f"Le film n° {choix + 1} possede desormais {films_list[choix]['places']} places")
                new_place.set(films_list[choix]['places'])
            else:
                print("Reservation impossible !")
                new_place.set("Complet")


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
        print(f"Film n° {numero} : {titre}, heure : {heure}, places dispo : {places}")

        place_var = StringVar()
        place_var.set(places)

        titre_label = Label(fenetre, text=titre)
        titre_label.grid(row=numero, column=0)

        heure_label = Label(fenetre, text=heure)
        heure_label.grid(row=numero, column=1)

        place_label = Label(fenetre, textvariable=place_var)
        place_label.grid(row=numero, column=2)

        book_button = Button(fenetre, text="Reserver")
        book_button.grid(row=numero, column=3)
        book_button.config(command=lambda num=numero, new_place=place_var: click_button(num, new_place))

    fenetre.mainloop()
