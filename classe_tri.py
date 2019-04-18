#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

class Etudiant:

    def __init__(self, nom, age, moyenne):
        
        self.nom = nom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):

        return "Etudiant {} : age : {}, moyenne {}".format(self.nom, self.age, self.moyenne)

class LigneInventaire:


    """Classe représentant une ligne d'un inventaire de vente.


    Attributs attendus par le constructeur :

        produit -- le nom du produit

        prix -- le prix unitaire du produit

        quantite -- la quantité vendue du produit.


    """


    def __init__(self, produit, prix, quantite):

        self.produit = produit

        self.prix = prix

        self.quantite = quantite


    def __repr__(self):

        return "<Ligne d'inventaire {} ({}X{})> \n".format(

                self.produit, self.prix, self.quantite)
