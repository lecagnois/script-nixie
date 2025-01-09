# -- coding: utf-8 --
def bdamis(nom,date):  
    datevenu = time.strftime("%d/%m/%Y")
    # cas de la date en alpha
    date = date.encode('utf-8')
    nom = nom.encode('utf-8')
    date= date.replace("le","").strip()
    date = date.replace("janvier", "01")
    date = date.replace("février", "02")
    date = date.replace("mars", "03") 
    date = date.replace("avril", "04") 
    date = date.replace("mai", "05") 
    date = date.replace("juin", "06") 
    date = date.replace("juillet", "07") 
    date = date.replace("août", "08")
    date = date.replace("septembre", "09")
    date = date.replace("octobre", "10")   
    date = date.replace("novembre", "11")
    date = date.replace("décembre", "12")        
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
            if len(jour.strip())==1:
                jour = ("0" + date[0:2].strip())  # ajout d un 0 si < 10
            mois=date[3:-5]
            if len(mois.strip())==1:
                mois = ("0"+date[3:-5].strip())
            anniversaire= jour.strip()+"-"+mois.strip()
            mail=""
            fromid=""
            valeurs = [[nom,jour,mois,annee,anniversaire,mail,fromid,datevenu]]
            #print(valeurs)
            f = open('data/bdamis.csv', 'a')
            for valeur in valeurs:
                ligne = ";".join(valeur) + "\n"
                f.write(ligne)
            f.close()
            #i01.speakBlocking(u"J'ai ajouté "+nom+ u" a la liste de tes amis. Tu devra compléter avec son id et son mail")  
            i01_chatBot.getResponse("ADD_FRIENDS")
        f.close()
                
    else:
        #création du fichier bdamis si inexistant     
        entetes = [u'PRENOM',u'JOUR',u'MOIS',u'ANNEE',u'ANNIVERSAIRE',u'ADRESSE MAIL',u'FROM ID',u'DATEVENU']
        annee=date[-4:]
        jour = date[0:2]
        if len(jour.strip())==1:
            jour = ("0"+ date[0:2].strip())  # ajout d un 0 si < 10
        mois=date[3:-5]
        if len(mois.strip())==1:
            mois = ("0"+date[3:-5].strip())
        anniversaire= jour.strip()+"-"+mois.strip()
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
    f.close()

    
    
        
    
    
