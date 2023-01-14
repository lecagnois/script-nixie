import csv

def planning():
	#declaration de varaibles 
	fname = "c:/planning.csv"
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
			i01.mouth.speakBlocking("planning du" + time.strftime('%d %m %Y'))
			sleep(2)
			for rdv in dataJ:
				i01.speakBlocking (rdv[2]+" "+rdv[3]+" "+rdv[4])
				sleep(2)
		else :
			i01.speakBlocking ("rien ce jour")
			sleep(2)

		if len(dataJ2) > 0 :
			i01.speakBlocking("demain")
			sleep(1)
			for rdv in dataJ2:
				i01.speakBlocking (rdv[2]+" "+rdv[3]+" "+rdv[4])
				sleep(2)
		else :
			i01.speakBlocking ("demain pas de rendez vous")
			sleep(2)
	finally:
		# Fermeture du fichier source
		file.close()