#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

# afficher le type iterateur

ma_chaine = "test"
iterateur_chaine = iter(ma_chaine)
print(iterateur_chaine)

# afficher toutes les iterations et l'exception stopIteration
print(next(iterateur_chaine))
print(next(iterateur_chaine))
print(next(iterateur_chaine))
print(next(iterateur_chaine))
print(next(iterateur_chaine))
