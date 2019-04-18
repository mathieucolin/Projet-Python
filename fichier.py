#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

import pickle

mon_fichier = open("fichier_test.txt", "r")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()

score = {
    "Joueur 1":50,
    "Joueur 2":30,
    "Joueur 3":60,
}

with open("fichier_test.txt", "w") as mon_fichier:
    contenu = mon_fichier.write("coucou")
    
with open("fichier_test.txt", "r") as mon_fichier:
    contenu = mon_fichier.read()

with open("donnees", "wb") as mon_objet:
    mon_pickler = pickle.Pickler(mon_objet)
    mon_pickler.dump(score)

with open("donnees", "rb") as mon_objet:
    mon_unpickler = pickle.Unpickler(mon_objet)
    score = mon_unpickler.load()
    print(score)
