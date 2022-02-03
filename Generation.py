# Clem #

#### Import librairies ####

import tkinter as tk
import random as rd


#### Constantes ####

HEIGHT = 600 # Hauteur
WIDTH = 600 # Largeur
N = 100 # Grille

# Paramètre de l'automate :
# Probabilité d'être un mur 
P = 1

#### Fonctions ####

def init_terrain():
    """Initialisation du terrain :"
    initialiser une liste à 2D de taille N telle que la case de coordonées (i,j) vaut l si il y a un mur dessus et 0 sinon
    initialisation de la liste carrée grille à 2D de taille N ... telle que la case de coordonnées (i,j) contient l'ider.. du carré dessiné
    Une case est un mur avec une probabilité
    """
    grille = []
    for i in range(N):
        grille.append([0]*N)
        print(grille)

#### Parti principale ####

## Création Widgets ##
racine = tk.Tk()
racine.title("Generation de Karen")
canvas = tk.Canvas(racine, height = HEIGHT, width= WIDTH)

button = tk.Button("Salut")
button.grid(row = 0, column = 1)
## Placement Widgets ##
canvas.grid(row = 0, column = 1)

## Boucle principale ##
racine.mainloop()

init_terrain()