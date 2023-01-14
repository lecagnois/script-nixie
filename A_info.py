# -- coding: utf-8 --
import urllib
import random

# votre cles nesapi google
cles = "entrer votre cles ici "

def info(nombre):
    
	try:
		
		#lecture du flux de API new adresse google 10 news
		url = urllib.urlopen("http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey="+cles)
		f = url.read()
		# creation tableau a partir de API 
		tableau = f[1:10000].decode('utf-8').split('"')
		#tableau = f[1:10].decode('utf-8').split('"')
		#print(f)
		#print(tableau)
		# creation tableau avec uniquement les titres et contenu
		Mnew = []
		# remplissage du tableau 
		i=0
		while i < len(tableau):
			if (tableau[i]=="title"):
				Mnew.append(tableau[i+2]+" . "+tableau[i+6])
			i=i+1			
		#lecture des donnees en parametre le nombre d informations
		# si nombre = 1 alors  donne une information au hasard sinon le nombre informations demandé
	
		if nombre == "1" :
			i01.speakBlocking(Mnew[random.randint(1,(len(Mnew)))])
		else :
			i=0
			while i < int(nombre) :
				i01.speakBlocking(Mnew[i])
				sleep(5)
				i = i+1
			
	except IOError:
		i01.speakBlocking("le serveur de nouvelles est hors service")
	except OSError:
		i01.speakBlocking("oups il y a une erreur OS")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur de valeur ")
	except:
		print(sys.exc_info()[0])
		raise