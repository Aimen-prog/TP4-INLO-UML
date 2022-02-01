#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Main execution program
"""

__author__ = 'Aimen CHERIF'

from collections import Counter

from etudiants import Note, Cours , Personne ,Etudiant

"""
Programme principal

"""

if __name__ == "__main__":

    etud1 = Etudiant("4340","Paul", "Dupont", "54554", "pl@mail.fr", 2019, ["anglais","math", "info"],[14,12,15])
    etud1.calculMoyenneGenerale()
    etud1.matieresSansNote()
   
    etud2 = Etudiant("4114","Alain", "Connu", "54554", "al@mail.fr", 2019, ["anglais","math","info"],[0,4,10])
    etud2.calculMoyenneGenerale()
    etud2.matieresSansNote()
  
    
    #moyenne par matiere : ( Normalement dans classe matiére )
    
    res1=etud1.toDict()
    res2=etud2.toDict()
    moyenne_matiere = dict(Counter(res1)+Counter(res2))
    for keys in moyenne_matiere :
        moyenne_matiere[keys]=moyenne_matiere[keys] / Etudiant.count  
    print(moyenne_matiere)
    

    
    
    
    
