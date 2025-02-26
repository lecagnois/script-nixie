# -- coding: utf-8 --

def Lire_planning():
    if os.path.exists('data/planning.csv'):
        #declaration de varaibles 
        fname = "data/planning.csv"
        file = open(fname, "r")
        dataJ=[]  # tableau Jour J
        dataJ2=[]  # tableau Jour J+1
        try :
            # Creation du lecteur CSV.
            reader = csv.reader(file,delimiter=";")
            # Boucle lecture lignes une par une.
            for row in reader:
                #print(row)
                # extraire dans tableau dataJ les donnees du jour J
                if (row[0]) ==  time.strftime('%d/%m/%Y') and (row[0]) != "" :
                    dataJ.append(row)
                    nbrdvJ = len(dataJ)
                # extraire dans tableau dataJ2 les donnees du jour + 1    
                if (row[0]) ==  time.strftime(str(int(time.strftime('%d'))+1)+'/%m/%Y') and (row[0]) != "" :
                    dataJ2.append(row)
                    nbrdvJ2 = len(dataJ2)
            if len(dataJ) > 0 :
                i01.speakBlocking(u"Voici le planning du, " + time.strftime('%d %m %Y') +u", j'ai trouvé : "+ str(nbrdvJ) + " rendez-vous")
                for rdv in dataJ:
                    i01.speakBlocking (rdv[1])
            else :
                i01_chatBot.getResponse("RDV_NUL")
            if len(dataJ2) > 0 :
                i01.speakBlocking(u"demain, j'ai trouvé : " + str(nbrdvJ2) + "rendez-vous" )
                for rdv in dataJ2:
                    i01.speakBlocking (rdv[1])
            else :
                i01_chatBot.getResponse("DEMAIN_NO_RDV")
        finally:
            # Fermeture du fichier source
            file.close()
    else:
        #création du fichier planning.csv
        i01_chatBot.getResponse("BD_PLANNING_KO")
        entetes = [u'DATE',u'MOTIF']
        f = open('data/planning.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        f.close()

def Ajout_planning(date_rdv,motif):
    if os.path.exists('data/planning.csv'):
        date_rdv = date_rdv.replace(u"1er", u"01").replace(u"é",u"e").replace(u"û",u"u")
        datedujour = datetime.now().date()
        # Expression régulière pour détecter différents formats de date
        pattern = r"\b(\d{1,2})\s*(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre|\/|-)\s*(\d{4})\b"
        pattern2 = r"\b(\d{1,2})\s+(\d{1,2})\s+(\d{4})\b"
        match = re.search(pattern, date_rdv, re.IGNORECASE)
        match2 = re.search(pattern2, date_rdv)
        #print(match.group(0))
        # cas date mois en lettre
        if match:
            jour = str(match.group(1))
            mois_str = date_rdv[match.start(2):match.end(2)].lower() # Mois en minuscules
            annee = str(match.group(3))
            # Convertir le mois en nombre
            mois_nombres = {
                'janvier': 1, 'fevrier': 2, 'mars': 3, 'avril': 4,
                'mai': 5, 'juin': 6, 'juillet': 7, 'aout': 8,
                'septembre': 9, 'octobre': 10, 'novembre': 11, 'decembre': 12}
            # Gérer les formats avec des séparateurs
            if mois_str in mois_nombres:
                mois = str(mois_nombres[mois_str])
                date_obj = datetime.strptime(jour+"/"+mois+"/"+annee, "%d/%m/%Y").date()
            else:
                i01_chatBot.getResponse("DATE_KO")

        # cas date en chiffre
        if match2:
            jour = str(match2.group(1))
            mois = str(match2.group(2))
            annee = str(match2.group(3))
            date_obj = datetime.strptime(jour+"/"+mois+"/"+annee, "%d/%m/%Y").date()
            
         # cas date incomplete
        if match== None and match2 == None :
            i01_chatBot.getResponse("DATE_KO")
        else :
            # on teste la date du jour avec la date envoye et ajoute valeur dans planning.csv
            if date_obj > datedujour or date_obj == datedujour :
                date_string = date_obj.strftime("%d/%m/%Y")
                valeurs = [[date_string,motif.encode("utf_8")]]
                f = open('data/planning.csv', 'a')
                for valeur in valeurs:
                    ligne = ";".join(valeur) + "\n"
                    f.write(ligne)
                f.close()
                i01_chatBot.getResponse("ADD_PLANNING")
            else:
                i01_chatBot.getResponse("DATE_KO")

    else:
        #création du fichier planning.csv
        i01_chatBot.getResponse("BD_PLANNING_KO")
        entetes = [u'DATE',u'MOTIF']
        f = open('data/planning.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        f.close()