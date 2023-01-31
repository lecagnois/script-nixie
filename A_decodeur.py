# -- coding: utf-8 --
import urllib
import sys
import socket

adresseip = "192.168.1.19:8080"
ipsocket =  "192.168.1.19"
port = 8080

def decodeur(commande):
	try:
		# verifier si serveur actif
		#i01.speakBlocking(u"je vérifie si le décodeur est allumé" )
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((ipsocket, port))
		if (commande == "10"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+ adresseip+'/remoteControl/cmd?operation=01&key=512&mode=0'
			urllib.urlopen(url)
		if (commande == "11"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)		
		if (commande == "12"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)		
		if (commande == "13"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=515&mode=0'
			urllib.urlopen(url)		
		if (commande == "14"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=516&mode=0'
			urllib.urlopen(url)		
		if (commande == "15"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=517&mode=0'
			urllib.urlopen(url)		
		if (commande == "16"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=518&mode=0'
			urllib.urlopen(url)		
		if (commande == "17"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=519&mode=0'
			urllib.urlopen(url)		
		if (commande == "18"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=520&mode=0'
			urllib.urlopen(url)		
		if (commande == "19"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=521&mode=0'
			urllib.urlopen(url)		
		if (commande == "20"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=512&mode=0'
			urllib.urlopen(url)		
		if (commande == "21"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=513&mode=0'
			urllib.urlopen(url)		
		if (commande == "22"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)		
		if (commande == "23"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=515&mode=0'
			urllib.urlopen(url)		
		if (commande == "24"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=516&mode=0'
			urllib.urlopen(url)		
		if (commande == "25"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=517&mode=0'
			urllib.urlopen(url)		
		if (commande == "26"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=518&mode=0'
			urllib.urlopen(url)		
		if (commande == "27"):
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=514&mode=0'
			urllib.urlopen(url)
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key=519&mode=0'
			urllib.urlopen(url)		
		else:
			url='http://'+adresseip+'/remoteControl/cmd?operation=01&key='+commande+'&mode=0'
			urllib.urlopen(url)
		
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except socket.error:
		i01.speakBlocking(u"le decodeur est hors service ")
	except:
		print(sys.exc_info()[0])
		raise