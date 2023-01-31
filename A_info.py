# -- coding: utf-8 --
#from __future__ import unicode_literals
import urllib
import random
import sys


macles="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def info(nombre):
	try:
		#lecture du flux de API new adresse google 10 news
		url = urllib.urlopen("http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey="+macles)
		#f = urllib2.urlopen("http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxx")
		f = url.read()
		# creation tableau a partir de API 
		tableau = f[1:10000].decode('utf-8').split('"')
		# creation tableau avec uniquement les titres et description
		Mnew = []
		# remplissage du tableau champ tittle , description , (content +" : " + tableau[i+22])
		i=0
		while i < len(tableau):
			if (tableau[i]=='title'):
				Mnew.append(tableau[i+2]+' : '+tableau[i+6])
			i=i+1			
		#lecture des donnees en parametre le nombre d informations
		# si nombre = 1 alors  donne une information au hasard sinon le nombre informations demandé < au tableau
		if ( int(nombre) <= (len(Mnew)) ):
			if nombre == "1" :
				#donne une information au hasard de la liste -1 et supprime les guillements vu codage
				i01.speakBlocking(Mnew[random.randint(1,(len(Mnew)-1))].replace(u'\u2019', ""))
			else :
				i=0
				while i < int(nombre) :
					print(Mnew[i])
					i01.speakBlocking((Mnew[i]).replace(u'\u2019', ""))
					sleep(5)
					i = i+1
		else:
			i01.speak(u"Le nombre de nouvelles est trop élevé")
   
	except IOError:
		i01.speakBlocking(u"le serveur de nouvelles est hors service ou la clés est périmé")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur de valeur ")
	except:
		print(sys.exc_info()[0])
		raise