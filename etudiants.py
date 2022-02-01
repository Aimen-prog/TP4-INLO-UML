#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Aimen CHERIF
"""

import re
from collections import Counter


"""

calculer la moyenne par matière
calculer la moyenne générale d’un élève
afficher les matières sans notes d'un élève



"""

class Note :
    def __init__(self, note_matiere):
        if note_matiere is None :
            self.note_matiere=note_matiere
        elif type(note_matiere) == float or int:
            self.note_matiere=note_matiere
        else:
            raise Exception("Invalid mark, should be numeric")

    def get_note(self):
        return self._note_matiere

    def set_note(self, note):
        self._note_matiere = note

    def __str__(self):
        return print(f'{self.note_matiere}')


class Cours :
    def __init__(self, identifiant_cours, nom_cours ):
        if identifiant_cours is None :
            self.identifiant_cours=identifiant_cours
        elif type(identifiant_cours) == str and len(identifiant_cours.replace(" ", "")) > 0:
            self.identifiant_cours=identifiant_cours
        else:
            raise Exception("Invalid subject id, should be str")

        if nom_cours is None :
            self.nom_cours=nom_cours
        elif type(nom_cours) == str and nom_cours.isalpha() and len(nom_cours.replace(" ", "")) > 0:
            self.nom_cours=nom_cours
        else:
            raise Exception("Invalid subject name, should be str")

    def get_cours(self):
        return self._nom_cours

    def set_cours(self, cours):
        self._nom_cours = cours




class Personne:

    def __init__(self,identifiant,nom,prenom,num_telephone,adresse_mail):  

        if type(identifiant) == str and len(identifiant.replace(" ", "")) > 0:
            self.identifiant = identifiant
        else:
            raise Exception("Invalid id, should be str type")

        if type(nom) == str and len(nom.replace(" ", "")) > 0:
            self.nom = nom
        else:
            raise Exception("Invalid last name, should be str type")

        if type(prenom) == str and len(prenom.replace(" ", "")) > 0:
            self.prenom = prenom
        else:
            raise Exception("Invalid first name, should be str type")

        if type(num_telephone) == str and num_telephone.isnumeric() and len(num_telephone.replace(" ", "")) > 0:
            self.num_telephone = num_telephone
        else:
            raise Exception("Invalid mobile number, should be str type and numeric")
            
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, adresse_mail)):
            self.adresse_mail=adresse_mail
        else:
            raise Exception("Invalid e-mail format")


    def afficher_fiche_signaletique(self):
        print(self.prenom,self.num_telephone,self.adresse_mail)




class Etudiant(Personne):

    count=0
    def __init__(self, identifiant,nom,prenom,num_telephone,adresse_mail, annee_entree, cours=[], notes=[]):
        super().__init__(identifiant,nom,prenom,num_telephone,adresse_mail)

        if type(annee_entree) == int and annee_entree >= 2014 and annee_entree <= 2022 :
            self.annee_entree=annee_entree
        else :
            raise Exception("Invalid year of class entry")

        self.cours= cours
        self.notes= notes

        if len(cours)==len(notes):
            pass
        else :
            raise Exception("Each subject needs to have a mark")

        Etudiant.count = Etudiant.count + 1 #count number of students


    def add_cours(self, cours):

        if isinstance(cours, Cours) and cours not in self.cours:
            self.cours.append(cours)
        else:
            raise Exception("Invalid course/subject name")


    def add_note(self, note):

        if isinstance(note, Note):
            self.notes.append(note)
        else:
            raise Exception("Invalid mark")



    def calculMoyenneGenerale(self) : #moy generale etudiant
        total=0
        for note in self.notes :
            if note is None :
                pass
            else :
                total+=note
        print( total/len(self.notes))


    def matieresSansNote(self) :  #matieres sans notes de l'eleve
        non_note=[]
        for i, j in zip(self.cours, self.notes):
            if j is None:
                non_note.append(i)
            else :
                continue
        if len(non_note)==0 :
            print ("There are no subjects with missing marks")
        else :
            print(non_note, "is/are subjects(s) with no marks")


    def toDict(self) : #moyenne par matiére
        res = {}
        for key in self.cours:
            for value in self.notes:
                res[key] = value
                self.notes.remove(value)
                break
        return(res)
