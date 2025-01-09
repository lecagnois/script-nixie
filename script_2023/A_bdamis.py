# -- coding: utf-8 --
import csv
import os

def bdamis(nom,date):  
    # si fichier bdamis existe  
    if os.path.exists('data/bdamis.csv'):
        
        #verification doublon
        flag = 0
        f = open('data/bdamis.csv', 'r')
        # Creation du lecteur CSV.
        reader = csv.reader(f,delimiter=";")
	    # Boucle lecture lignes une par une colonne 0.
        for ligne in reader:
            print(ligne[0])
            if (nom.upper() == ligne[0]):
                i01.speakBlocking(u"jai déjà le prénom de "+nom + u" je ne peux pas l'ajouter à la base de donnée.")
                flag = 1
        f.close()
        #ajout des donnees si prenom inexistant   
        if flag == 0 :
            annee=date[-4:]
            jour = date[0:2]
            mois=date[3:-5]
            anniversaire= jour+"-"+mois
            mail=""
            fromid=""
            valeurs = [[nom.upper(),jour,mois,annee,anniversaire,mail,fromid]]
            f = open('data/bdamis.csv', 'a')
            for valeur in valeurs:
                ligne = ";".join(valeur) + "\n"
                f.write(ligne)
            f.close()
            i01.speakBlocking(u"J'ai ajouté "+nom+ u" a la liste de tes amis. Tu devra compléter avec son mail.")  
                
    else:
        #création du fichier bdamis
        entetes = [u'PRENOM',u'JOUR',u'MOIS',u'ANNEE',u'ANNIVERSAIRE',u'ADRESSE MAIL',u'FROM ID']
        annee=date[-4:]
        jour=date[0:2]
        mois=date[3:-5]
        anniversaire= jour+"-"+mois
        mail=""
        fromid=""
        valeurs = [[nom.upper(),jour,mois,annee,anniversaire,mail,fromid]]
        f = open('data/bdamis.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
        i01.speakBlocking(u"J'ai ajouté " +nom+ u" a la liste de tes amis. Tu devra compléter avec son mail.")   
    
