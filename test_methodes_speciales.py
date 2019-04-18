#!/usr/bin/Python-3.7.0   
# -*-coding:Utf-8 -*

from classes_methodes_speciales import *

d1 = Duree(3,5)
print(d1) 

d2 = d1 +128
print(d2)

d3 = 4 + d2
print(d3)

d3 += 8
print(d3)

if d3 == d2:
    print("durée d1 et d2 égales")
else:
    print("durée d3 et d2 pas égales")

if (d3 > d2):
    print("d3 est supérieur à d2")
else:
    print("d3 n'est pas supérieur à d2")