#!/usr/bin/python2.7    
# -*-coding:Utf-8 -*

def afficher_flottant(flottant):
    if(type(flottant) is not float):
        raise TypeError("Le paramètre doit être un flottant")

    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")

    return ",".join([partie_entiere, partie_flottante[:3]])