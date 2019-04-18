#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

class Zdict:

    def __init__ (self):
        self._dictionnaire = {}

    def __getitem__(self, index):
        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        self._dictionnaire[index] = valeur 

class Duree:

    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec
    
    def __str__ (self):
        return "Duree : {0:02}:{1:02}".format(self.min, self.sec)

    def __add__ (self, objet_a_ajouter):
        nouvelle_duree = Duree()

        nouvelle_duree.sec = self.sec
        nouvelle_duree.min = self.min

        nouvelle_duree.sec += objet_a_ajouter

        if nouvelle_duree.sec > 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        return nouvelle_duree

    def __radd__ (self, objet_a_ajouter):

        return self + objet_a_ajouter
    
    def __iadd__ (self, objet_a_ajouter):
        self.sec += objet_a_ajouter
        if self.sec > 60:
            self.min = self.sec // 60
            self.sec = self.sec % 60
        
        return self

    def __eq__ (self, objet_a_comparer):
        return self.sec == objet_a_comparer.sec and self.min == objet_a_comparer.min

    def __gt__ (self, objet_a_comparer):
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = objet_a_comparer.sec + objet_a_comparer.min * 60

        return nb_sec1 > nb_sec2