#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

from classes import *

man = Personne("Oliv", "dupont")
print(man.nom, man.prenom)

a = Compteur()
print(Compteur.objets_crees)
b = Compteur()
print(Compteur.objets_crees)

mon_tableau = TableauNoir()

mon_tableau.ecrire("message 1")
mon_tableau.ecrire("aaaapero 2")
mon_tableau.lire()
mon_tableau.effacer()
mon_tableau.lire()

# help(TableauNoir) 

print(man.lieu_residence)
man.lieu_residence = "Berlin"
print(man.lieu_residence)
print(man)