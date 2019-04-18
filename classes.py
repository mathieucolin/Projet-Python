#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

class Personne:

    def __init__(self, nom, prenom):
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 33
        self._lieu_residence = "Paris"
    
    def __repr__(self):
        return "Personne : nom ({}), prénom ({}) et age ({}).".format(self.nom, self.prenom, self.age)
    
    def _get_lieu_residence(self):
        print("accès à l'attribut ")
        return self._lieu_residence
    
    def _set_lieu_residence(self, nouveau_lieu):
        print("modification de lieu ")
        self._lieu_residence = nouveau_lieu

    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

class Compteur:

    objets_crees = 0

    def __init__(self):
        Compteur.objets_crees += 1

    def combien(cls):
        print("Jusqu'à présent {} objets ont ete crees".format(cls.objets_crees))
    
    combien = classmethod(combien)

    def afficher():
        print("fonction statique")

    afficher = staticmethod(afficher)

class TableauNoir:
  
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""
        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""
       
        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""
