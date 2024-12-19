# -- coding: utf-8 --
import csv
import os
import datetime
    

def bdamis(nom,date):  
    datevenu = (datetime.date.today()).strftime("%d/%m/%Y")
    try:
        # Parse la chaîne pour créer un objet datetime cas de la date non numerique
        date_obj = datetime.datetime.strptime(date, "%d %B %Y")
        # Formatte l'objet datetime dans le format souhaité 01 01 2000
        date_formattee = date_obj.strftime("%d %m %Y")
        date = date_formattee
        #print (date)
    except ValueError:
        #print(u"Format de date au format numérique : "+date)
        date = date
        
    # si fichier bdamis existe  
    if os.path.exists('data/bdamis.csv'):
        
        #verification doublon
        flag = 0
        f = open('data/bdamis.csv', 'r')
        # Creation du lecteur CSV.
        reader = csv.reader(f,delimiter=";")
	    # Boucle lecture lignes une par une colonne 0.
        for ligne in reader:
            #print(ligne[0])
            if (nom == ligne[0]):
                 # get responce in file bd_amis.xml
                i01_chatBot.getResponse("FIRST_NAME_ALREADY_EXISTS")
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
            valeurs = [[nom,jour,mois,annee,anniversaire,mail,fromid,datevenu]]
            f = open('data/bdamis.csv', 'a')
            for valeur in valeurs:
                ligne = ";".join(valeur) + "\n"
                f.write(ligne)
            f.close()
            #i01.speakBlocking(u"J'ai ajouté "+nom+ u" a la liste de tes amis. Tu devra compléter avec son id et son mail")  
            i01_chatBot.getResponse("ADD_FRIENDS")
                
    else:
        #création du fichier bdamis       
        entetes = [u'PRENOM',u'JOUR',u'MOIS',u'ANNEE',u'ANNIVERSAIRE',u'ADRESSE MAIL',u'FROM ID',u'DATEVENU']
        annee=date[-4:]
        jour=date[0:2]
        mois=date[3:-5]
        anniversaire= jour+"-"+mois
        mail=""
        fromid=""
        valeurs = [[nom,jour,mois,annee,anniversaire,mail,fromid,datevenu]]
        f = open('data/bdamis.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
        # get responce in file bd_amis.xml
        i01_chatBot.getResponse("ADD_FRIENDS")

    
    
        
    
    
