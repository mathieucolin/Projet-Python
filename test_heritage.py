#!/usr/bin/python3.7    
# -*-coding:Utf-8 -*

from classe_heritage import *

agent = AgentSpecial("OSS","117")

print(agent.nom)
print(agent)

print(agent.prenom)

print("Agent special est elle une sous classe de Personne ? :", issubclass(AgentSpecial, Personne))
print("Agent special est elle une sous classe de objet ? :", issubclass(AgentSpecial, object))
print("Personne est elle une sous classe de objet ? :", issubclass(Personne, object))
print("Personne est elle une sous classe de Agent special ? :", issubclass(Personne, AgentSpecial))

print("agent est une instance de Agent special ? :", isinstance(agent, AgentSpecial))
print("agent est une instance de Personne ? : ", isinstance(agent, Personne))
print("agent est une instance d'objet ? : ", isinstance(agent, object))

# Utilisation de l'héritage avec les exceptions

# exception = monException("Oups j'ai tout pete")
# raise exception

# Exceptions avec plusieurs paramètres

exception_fichier = erreurAnalyseFichier("plop.conf", "32", "tas tout pete")
raise exception_fichier