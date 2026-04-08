

import math


print("*"*25,"Exercice 01","*"*25)
# Création de la classe Livre
class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def lire(self):
        print(f"Je lis : {self.titre} de {self.auteur}")
    def __str__(self):
        return f"Livre : {self.titre} - {self.auteur} ({self.pages} pages)"

    def __len__(self):
        return self.pages


    def __eq__(self, autre):
        return self.titre == autre.titre and self.auteur == autre.auteur

l1 = Livre("Crime et Châtiment", "Dostoevsky", 430)
l2 = Livre("Crime et Châtiment", "Dostoevsky", 500)

l1.lire()
l2.lire()

print(l1)           
print(len(l1))      
print(l1 == l2) 

print("*"*25,"Exercice 02","*"*25)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_point(self):
        print(f"({self.x}, {self.y})")

    def distance(self, autre):
        return math.sqrt((self.x - autre.x)**2 + (self.y - autre.y)**2)

    def milieu_segment(self, autre):
        mx = (self.x + autre.x) / 2
        my = (self.y + autre.y) / 2
        return Point(mx, my)

    def translation(self, deplacement):
        self.x += deplacement.dx
        self.y += deplacement.dy


    def projection_x(self):
        return Point(self.x, 0)


    def projection_y(self):
        return Point(0, self.y)


# Classe Deplacement
class Deplacement:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy




xA = float(input("Entrez x de A: "))
yA = float(input("Entrez y de A: "))
xB = float(input("Entrez x de B: "))
yB = float(input("Entrez y de B: "))

A = Point(xA, yA)
B = Point(xB, yB)

#Affichage des points
print("Coordonnées du point A:", end=" ")
A.afficher_point()
print("Coordonnées du point B:", end=" ")
B.afficher_point()

#Distance entre A et B
d = A.distance(B)
print(f"Distance entre A et B: {d}")

#Milieu du segment AB
milieu = A.milieu_segment(B)
print("Milieu du segment AB:", end=" ")
milieu.afficher_point()

#Projection de A sur l'axe des X
projX = A.projection_x()
print("Projection de A sur l'axe X:", end=" ")
projX.afficher_point()

#Saisie du déplacement
dx = float(input("Entrez le déplacement selon X: "))
dy = float(input("Entrez le déplacement selon Y: "))
dep = Deplacement(dx, dy)

#Nouvelle position après déplacement
A.translation(dep)
B.translation(dep)
print("Nouvelle position de A:", end=" ")
A.afficher_point()
print("Nouvelle position de B:", end=" ")
B.afficher_point()

#Nouvelle projection de A sur l'axe Y
projY = A.projection_y()
print("Nouvelle projection de A sur l'axe X:", end=" ")
projY.afficher_point()







