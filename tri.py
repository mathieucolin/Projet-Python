#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

from classe_tri import *
from operator import itemgetter, attrgetter

prenoms = ["Jacques","Laure", "André", "Victoire", "Albert", "Sophie"]

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]


classes_etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

inventaire = [

    LigneInventaire("pomme rouge", 1.2, 19),

    LigneInventaire("orange", 1.4, 24),

    LigneInventaire("banane", 0.9, 21),

    LigneInventaire("poire", 1.2, 24),

]

# différence sort et sorted

print(sorted(prenoms))
print(prenoms)
prenoms.sort()
print(prenoms)

#tri avec lambda sur une liste
print(sorted(etudiants, key = lambda colonnes : colonnes[2]))

#tri avec lambda sur une classe
print(sorted(classes_etudiants, key = lambda etudiants:etudiants.moyenne))

#tri avec itemgetter sur une liste
print(sorted(etudiants, key = itemgetter(2)))

#tri avec attrgetter sur une classe
print(sorted(classes_etudiants, key = attrgetter("moyenne")))

#tri avec attrgetter et deux paramètres sur une classe
print(sorted(classes_etudiants, key = attrgetter("age", "moyenne")))

#chainage de tris exemple :

sorted(inventaire, key=attrgetter("prix", "quantite"))

##################

inventaire.sort(key=attrgetter("quantite"), reverse=True)
print(inventaire)

print(sorted(inventaire, key=attrgetter("prix")))