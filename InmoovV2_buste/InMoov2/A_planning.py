# -- coding: utf-8 --

def planning():
    
	if os.path.exists('data/planning.csv'):
     	#declaration de varaibles 
		fname = "data/planning.csv"
		file = open(fname, "r")
		dataJ=[]  # tableau de donnees
		dataJ2=[]
		try :
			# Creation du lecteur CSV.
			reader = csv.reader(file,delimiter=";")
			# Boucle lecture lignes une par une.
			for row in reader:
				#print(row)
				# extraire dans tableau dataJ les donnees du jour J
				if (row[0]) ==  time.strftime('%d/%m/%Y') and (row[0]) != "" :
					dataJ.append(row)
				# extraire dans tableau dataJ2 les donnees du jour + 1    
				if (row[0]) ==  time.strftime( str(int(time.strftime('%d'))+1)+'/%m/%Y') and (row[0]) != "" :
					dataJ2.append(row)
		
			if len(dataJ) > 0 :
				i01.speakBlocking("planning du" + time.strftime('%d %m %Y'))
				for rdv in dataJ:
					i01.speakBlocking (rdv[2]+" "+rdv[3]+" "+rdv[4])
			else :
				i01.speakBlocking ("rien ce jour")
			if len(dataJ2) > 0 :
				i01.speakBlocking("demain")
				for rdv in dataJ2:
					i01.speakBlocking (rdv[2]+" "+rdv[3]+" "+rdv[4])
			else :
				i01.speakBlocking ("demain pas de rendez vous")
		finally:
			# Fermeture du fichier source
			file.close()
	else:
		#création du fichier planning.csv
		i01.speakBlocking (u"La base de donnée n'existe pas, je vais la créer.")
		entetes = [u'DATE',u'JOUR',u'TYPE',u'INFO',u'HEURE']
		f = open('data/planning.csv', 'w')
		ligneEntete = ";".join(entetes) + "\n"
		f.write(ligneEntete)
		f.close()

