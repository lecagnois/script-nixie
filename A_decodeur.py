import urllib

#adresseip de votre decodeur orange
adresseip = "192.168.1.19:8080"
def decodeur(commande):
	try:
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
		
	except IOError:
		talk("le serveur est hors service ")
	except OSError:
		talkBlocking("oups il y a une erreur")
	except ValueError:
		talkBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise