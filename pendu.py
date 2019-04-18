#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

from donnees import*
from fonctions import*

lettres_trouvees = []
continuer_partie = 1

while continuer_partie:
    
    """récupération du mot au hasard"""
    
    mot = recup_mot()
    mot_joueur = ""
    utilisateur = recup_utilisateur()
    score = recup_fichier()
    print("liste des scores : {}".format(score))

    if utilisateur not in score.keys():
        print("Création d'un nouvel utilisateur ...")
        score[utilisateur] = 0
        print("Bienvenue {}, vous avez {} points".format(utilisateur, score[utilisateur]))

    else:
        print("Bienvenue {}, vous avez {} points".format(utilisateur, score[utilisateur]))

    while(mot_joueur != mot and coups_restant > 0):    
        
        print("Il vous reste {} coups a jouer pour le mot : {}".format(coups_restant, mot_joueur))
        
        """vérification de la lettre jouée"""
        lettre = recup_lettre()

        if lettre in lettres_trouvees:
            print("Vous avez deja joue cette lettre")

        elif lettre in mot:
            print("Lettre trouvee")            
            lettres_trouvees.append(lettre)
            coups_restant = coups_restant - 1
        else:
            print("echec")
            coups_restant = coups_restant - 1
        
        mot_joueur = recup_mot_masque(mot, lettres_trouvees)

    if(mot_joueur == mot):
        print("Felicitations vous avez gagne la partie ! Le mot etait bien {}".format(mot))
    
    else:
        print("Vous avez perdu")
    
    print("Enregistrement du score ...")
    score[utilisateur] = score[utilisateur] + coups_restant
    enregistrer_score(score)

    choix = input("Voulez vous continuer la partie ? (o/n)")
    choix.lower()
    if(choix == "o"):
        continuer_partie = 1
        coups_restant = 8
        lettres_trouvees = []
    else:
        continuer_partie = 0