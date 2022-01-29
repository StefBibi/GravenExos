import random

print("Bienvenu dans le jeu !")
print("Selectionner la difficulté : 1, 2 ou 3 ?")
diff = int(input())
print("Difficulté : ", diff)

liste =[]

for i in range(0, 3):
    liste.append(2)
    print(liste[i])

# Compteur de clé
keys = 0

# repeter les manches de jeu
while keys < 3:
    print("Vous avez 5 jarres devant vous. Choisissez 1,2,3,4 ou 5")

    # choix aleatoire de la jarre avec le serpent parmis les 5
    snake_jar = random.randint(1, 5)

    # entree du joueur
    choix = int(input())
    print("Choix du joueur, jarre n°", choix)

    # verification
    if choix != snake_jar:
        print(" Gagné, le serpent est en ", snake_jar)
        keys += 1
        print (" Vous avez ", keys, "/3 clés")
    else:
        print(" Perdu, un serpent apparait ")
        if keys > 0:
            keys -= 1
        print(" Vous avez " + str(keys) + "/3 clés")

print ("Tu deviens roi du temple !")
