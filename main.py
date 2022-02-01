#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Main execution program
"""

__author__ = 'Aimen CHERIF'

from collections import Counter

from etudiants import Etudiant

"""
Programme principal

"""

if __name__ == "__main__":

    etud = Etudiant("4340","Paul", "Dupont", "54554", "pl@mail.fr", 2019, ["sport","math", "info"],[None,8,1])
    etud.calculMoyenneGenerale()
    etud.matieresSansNote()
    print("\n")

    etud1 = Etudiant("1340","Sam", "Lee", "12254", "sm@mail.fr", 2017, ["anglais","math", "info"],[14,12,15])
    etud1.calculMoyenneGenerale()
    etud1.matieresSansNote()
    print("\n")

    etud2 = Etudiant("4114","Alain", "Connu", "78554", "al@mail.fr", 2019, ["anglais","math","info"],[0,4,10])
    etud2.calculMoyenneGenerale()
    etud2.matieresSansNote()
    print("\n")


    #moyenne par matiere : ( doit normalement etre dans la classe Matriere )
    #Cas seulement 2 etudiants (etud1 et etud2)

    res1=etud1.to_dict()
    res2=etud2.to_dict()
    moyenne_matiere = dict(Counter(res1)+Counter(res2))
    for keys in moyenne_matiere :
        moyenne_matiere[keys]=moyenne_matiere[keys] / Etudiant.count
    print("mean for each subject: ", moyenne_matiere)
