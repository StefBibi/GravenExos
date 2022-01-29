import random

print("Bienvenu dans le jeu !")
print("Vous avez 5 jarres devant vous. Choisissez 1,2,3,4 ou 5")

# choix aleatoire de la jarre avec le serpent parmis les 5
snake_jar = random.randint(1, 5)

# entree du joueur
choix = int(input())
print("Choix du joueur, jarre n°", choix)

# verification
if choix == snake_jar:
    print(" Perdu ")
else:
    print(" Gagné, le serpent est en ", snake_jar)
