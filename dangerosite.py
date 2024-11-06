import numpy as np
nb_lignes = 12
nb_colonnes = 16

xT_grid = np.zeros((nb_lignes, nb_colonnes))

for i in range (12) :
  for j in range(12) :
    xT_grid[i][j] = 0.05

for i in range(12) :
  if i<5 or i>6 :
    xT_grid[i][12] = 0.05
  else :
    xT_grid[i][12] = 0.08

for i in range(12) :
  if i<4 or i>7 :
    xT_grid[i][13] = 0.05
  elif i==4 or i==7 :
    xT_grid[i][13] = 0.10
  else :
    xT_grid[i][13] = 0.15

for i in range(12) :
  if i<3 or i>8 :
    xT_grid[i][14] = 0.05
  elif i==3 or i==8 :
    xT_grid[i][14] = 0.08
  elif i==4 or i==7 :
    xT_grid[i][14] = 0.15
  else :
    xT_grid[i][14] = 0.20


for i in range(12) :
  if i<3 or i>8 :
    xT_grid[i][15] = 0.05
  elif i==3 or i==8 :
    xT_grid[i][15] = 0.08
  elif i==4 or i==7 :
    xT_grid[i][15] = 0.15
  else :
    xT_grid[i][15] = 0.30

longueur_terrain = 120
largeur_terrain = 80

hauteur_cellule = largeur_terrain / nb_lignes
largeur_cellule = longueur_terrain / nb_colonnes

def dangerosite(x, y):
    if x < 0 or x > longueur_terrain or y < 0 or y > largeur_terrain:
        #raise ValueError("Les coordonnées sont en dehors du terrain")
        return 0

    if x == 120:
        return dangerosite(x-1,y)
    elif y == 80:
        return dangerosite(x,y-1)

    index_colonne = int(x // largeur_cellule)
    index_ligne = int(y // hauteur_cellule)

    return xT_grid[index_ligne, index_colonne]