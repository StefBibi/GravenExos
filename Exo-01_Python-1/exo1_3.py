import random

print("Bienvenu dans le jeu !")

# Choix du niveau de difficulté
print("Selectionner la difficulté : 1, 2 ou 3 ?")
level = int(input())
print("Difficulté : ", level)

# Compteur de clé
trousseau = 0

# repeter les manches de jeu
while trousseau < 3:
    print("Vous avez 5 jarres devant vous. Choisissez 1,2,3,4 ou 5")

    # tableau des jarres
    jars = ['K', 'k', 'k', 'k', 'k']
    # remplissage des jars selon la difficulte
    for i in range(0, level):
        jars[i] = 'S'
    # melande des jars de la liste
    """
    # ou autre possibilté de tableau de jarre
    snakes = ["S"] * level
    keys = ["k"] * 5 - level
    jars = snakes + keys   
    """
    random.shuffle(jars)
    print(jars)

    # entree du joueur
    choix = int(input())
    print("Choix du joueur, jarre n°", choix)

    # verification
    if jars[choix-1] == 'k':
        print(" Gagné, aucun serpent en ", choix)
        trousseau += 1
        print (" Vous avez ", trousseau, "/3 clés")
    else:
        print(" Perdu, un serpent apparait ")
        if trousseau > 0:
            trousseau -= 1
        print(" Vous avez " + str(trousseau) + "/3 clés")

print ("Tu deviens roi du temple !")
