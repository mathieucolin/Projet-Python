#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)

# parametres = dict()
# parametres = {"sep":" >> ", "end":" -\n"}
# print("Voici", "un", "exemple", "d'appel", **parametres)
# print("Voici un exemple", **parametres)
def fete():
    print("cest la fete")

def oiseau():
    print("oiseau")

dictionnaire = dict()
dictionnaire["fete"]=fete
dictionnaire["oiseau"]=oiseau

dictionnaire["oiseau"]()
