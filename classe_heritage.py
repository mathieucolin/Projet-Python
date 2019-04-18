#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

class Personne:

    def __init__(self, nom):
        self.nom = nom
        self.prenom = "Martin"
    
    def __str__(self):
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):

    def __init__(self, nom, matricule):
        Personne.__init__(self, nom)
        self.matricule = matricule

    def __str__(self):
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)
    
class monException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class erreurAnalyseFichier(Exception):
    def __init__(self, fichier, ligne, message):
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        return "[{}:{}] {}".format(self.fichier, self.ligne, self.message)
    
    