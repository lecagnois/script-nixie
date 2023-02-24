# -- coding: utf-8 --
import urllib

security.loadStore()
makey = security.getSecret("airvisual")
#a changer tous les ans

def airqualite(ville,region):
	if makey == None:
		i01.speakBlocking(u"Votre clés A P I est périmé ,ou non validé dans le service sécurity")
	else:
		try:
			#lecture du flux de API en parametres ville et region
			url = urllib.urlopen("https://api.airvisual.com/v2/city?city="+ville+"&state="+region+"&country=France&key="+makey)
			# exemple https://api.airvisual.com/v2/city?city=nice&state=paca&country=France&key=xxxxxxxxxxxxxxxxxxxxxxxxxx
			f = url.read()

			# creation tableau a partir de API airvisual et suppresion des virgules
			tableau = f.replace(","," ")[1:1000].decode('utf-8')
			#print(tableau)

			# extration des données dans des variables avec modification du type en entier
			Mqualite = int(tableau[(tableau.find('aqius'))+7:(tableau.find('aqius'))+10])
			Mhumide =  int(tableau[(tableau.find('hu'))+4:(tableau.find('hu'))+6])
			Mpression = int(tableau[(tableau.find('pr'))+4:(tableau.find('pr'))+8])
			Mtemperature = int(tableau[(tableau.find('tp'))+4:(tableau.find('tp'))+6])
			Mvitessevent =  int(tableau[(tableau.find('ws'))+4:(tableau.find('ws'))+5])
			#print type(Mqualite)
			#print (Mqualite)

			# test niveau de pollution
			if Mqualite < 50 :
				i01.speakBlocking("Le Niveau de pollution de "+ville+" est de  " + str(Mqualite) + u" . La qualité de l'air est juger satifaisante, et la pollution de l'air pose peu ou pas de risque")
			if Mqualite > 50 and Mqualite <= 100 :
				i01.speakBlocking("Niveau de pollution de " + ville + " est de : " + str(Mqualite) + u" La qualité de l'air est acceptable. Cependant, pour certains polluants, un trait petit nombre de personnes qui sont particulierement sensibles a la pollution de l'air peuvent avoir des soucis de santé modeste. Les enfants et les adultes actifs, ainsi que les personnes souffrant de maladies respiratoires, comme l'asthme, devraient limiter leur effort prolonger en pleine air")
			if Mqualite > 100 and Mqualite <= 150 :
				i01.speakBlocking("Niveau de pollution de "+ville+ "est de : " + str(Mqualite) + u" La qualité de l'air est mauvaise . les personnes sensibles peuvent avoir des effets sur leur santé. Le grand public n'est pas susceptible d'être affecté. Les enfants et les adultes actifs, ainsi que les personnes souffrant de maladies respiratoires, comme l'asthme, devraient limiter leur effort prolongé en pleine air")
			if Mqualite > 150 and Mqualite <= 200 :
				i01.speakBlocking("Niveau de pollution de "+ville+ " est de : " + str(Mqualite) + u" La qualité de l'air est mauvaise . Tout le monde peut commencer a ressentir des effets sur la santé; les membres des groupes sensibles peuvent ressentir des effets plus graves sur leur santé Les enfants et les adultes actifs, ainsi que les personnes souffrant de maladies respiratoires, comme l'asthme, devraient éviter les efforts prolongé a l'exterieur; tout le monde, en particulier les enfants, devrait limiter l'effort prolongé en pleine air")
			if Mqualite > 200 and Mqualite <= 300 :
				i01.speakBlocking("Niveau de pollution de "+ville+ "est de : " + str(Mqualite) + u" La qualité de l'air est très mauvaise . Avertissements de santé de conditions d'urgence . Toute la population est plus suceptible dêtre affecté")
			if Mqualite > 300 :
				i01.speakBlocking("Niveau de pollution de "+ville+ "est de : " + str(Mqualite) + u" La qualité de l'air est très dangereuse . Alerte de santé, tout le monde peut ressentir des effets de santé très graves . surtout éviter de sortir .")
				
			i01.speakBlocking(u"humidité de l'air est de " + str(Mhumide) +" pourcent")
			sleep(1)
			i01.speakBlocking(u"la préssion est de  " + str(Mpression) + " bar")
			sleep(1)
			i01.speakBlocking(u"la température est de " + str(Mtemperature) + u" degré")
			sleep(1)
			i01.speakBlocking("la vitesse du vent est de  " + str(Mvitessevent) +" KM/H")
					

		except IOError:
			i01.speakBlocking(u"je n'ai pas de capteur pour cette ville")
		except OSError:
			i01.speakBlocking("oups il y a une erreur OS")
		except ValueError:
			i01.speakBlocking(u"oups il y a une erreur de valeur ou clé invalide ")
		except:
			print(sys.exc_info()[0])
			raise
	