#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

import pickle
from random import choice
from donnees import *
from pathlib import Path

def recup_utilisateur():

    utilisateur = input("Entrez votre nom : ")
    utilisateur = utilisateur.capitalize()
    if not utilisateur.isalnum() or len(utilisateur) < 4:
        print("Nom d'utilisateur invalide")
        return recup_utilisateur()
    else:
        return utilisateur

def enregistrer_score(score):

    with open(nom_fichier, "wb") as fichier_ecriture:
        mon_pickler = pickle.Pickler(fichier_ecriture)
        mon_pickler.dump(score)


def recup_fichier():
    config = Path(nom_fichier)
    if config.is_file():
        with open (nom_fichier, "rb") as fichier_recup:
            mon_unpickler = pickle.Unpickler(fichier_recup)
            score = mon_unpickler.load()
            return score
    else:
        score = {}
        return score

def recup_mot():
    """récuprération d'un mot au hasard de la liste du fichier donnees"""
    return choice(liste_mots)

def recup_lettre():
    lettre = input("Choisissez une lettre : ")

    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas entre une lettre correcte")
        return recup_lettre()
    else: 
        return lettre

def recup_mot_masque(mot, lettres_trouvees):
    mot_masque = ""
    for lettres in mot:
        if lettres in lettres_trouvees:
            mot_masque += lettres
        else:
            mot_masque += "*"
    
    return mot_masque

