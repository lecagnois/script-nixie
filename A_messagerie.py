# -- coding: utf-8 --
import imaplib
import re
import email
import smtplib
from email import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import *
from email import encoders
from email.mime.base import *

def mailsend(amis,message):
	try:
		i01.speakBlocking(amis)
		# creation d un dictionnaire des amis
		dico = {"jean pierre":"son adresse mail","colette":"son adresse mail"}
		# message si pas trouver
		if (dico.get(amis) == None):
			print("Amis inconnu dans l annuaire")
			i01.speakBlocking("personne inconnu au bataillon")
		else:
			print (dico.get(amis))
			i01.speakBlocking(" fais parti de tes amis ")
			sleep(3)
			global ami 
			ami = (dico.get(amis))
			# supprimer le texte inutule
			message = message.strip("Si ok")[:-22]
			#print(message)
			#print(amis)
			#print(ami)
			envoi(message,ami)
			
	except IOError:
		talk("le serveur est hors service , mail non transmis")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

def envoi(message,adresse):
	try:
		codage = 'UTF-8' # <= modif
		fromaddr = "mail expediteur"
		toaddr = adresse
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Message de InMOOV"
		msg['Charset'] = codage  # <= modif
		msg['Content-Type'] = 'text/plain; charset=UTF-8' # <--modif
		body = message
		if ami == "mail destinataire":
			typetexte = 'text/plain' # <= modif
		else:
			typetexte = 'plain'
		msg.attach(MIMEText(body, typetexte, 'UTF-8')) # <= modif
		#msg.attach(MIMEText(body, 'text/plain'))
		
		# valeur du serveur smtp securise ou pas
		#server = smtplib.SMTP('smtp.gmail.com', 587)
		server = smtplib.SMTP('smtp-msa.orange.fr', 587)
		#server.starttls()
		server.login(fromaddr, "YOUR PASSWORD")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		sleep(3)
		i01.speakBlocking("mel transmis a " + ami)
		server.quit()
		server.close()
	
	except IOError:
		talk("le serveur est hors service , mail non transmis")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

def liremail(destinataire):
	try :
		# creation d un dictionnaire des amis
		dico = {"jean pierre":'(FROM "lecagnois")',"colette":'(FROM "collinette")', "robot":'(FROM "inmoov")'}
		# message si pas trouver
		if (dico.get(destinataire) == None):
			print("Amis inconnu dans l annuaire")
			i01.speakBlocking("personne inconnu au bataillon")
		else:
			mail = imaplib.IMAP4_SSL('imap.orange.fr')
			# imaplib module implements connection based sur protocol IMAPv4 
			mail.login('votre boite mail', 'votre mot de passe')
			mail.list() 
			mail.select('inbox') # Connecter a inbox.
			(status,nbMessages) = mail.select('INBOX')
			print("connecter inbox")
			
			#Rechercher message dans expediteur
			result, data = mail.uid('search', None, (dico.get(destinataire)))
			#result, data = mail.uid('search', None, '(FROM "lecagnois")')
			i = len(data[0].split()) # data[0] supprime espace
			Totalmsg = re.findall('\d+', str(nbMessages))[0]
			print (result + ' Nombre de messages = ' + str(Totalmsg))
			i01.speakBlocking("il y a  au total "+str(Totalmsg)+ " messages dans ta boite mail ")
			print("trouver : " +str(i))
			i01.speakBlocking("jai trouver " + str(i) + " message de " + destinataire )

			for x in range(i):
				latest_email_uid = data[0].split()[x] # ID unique étiquette sélectionnée
				result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
				# Récupérer le corps de courrier électronique pour l'ID donné
				raw_email = email_data[0][1]

				# boucle 1 
				raw_email_string = raw_email.decode('utf-8')
				# Convertit  d'octet en chaîne 
				email_message = email.message_from_string(raw_email_string)

				#boucler à travers toutes les multiparties disponibles dans le mail
				for part in email_message.walk():
					if part.get_content_type() == "text/plain": # ignore html
						body = part.get_payload(decode=True)
						print(body.decode('utf-8'))
						Mreponse = (body.decode('utf-8'))
						i01.speakBlocking("message " + str(x+1) +". "+ Mreponse)
					if part.get_content_type() == "multipart/mixed" : # ignore piece jointe
						 body = part.get_payload(decode=False)
						
					else:
						continue
        
			if i == 0 :
				print("pas de messages")
				sleep(4)
				i01.speakBlocking("a bientot")
				
			#fermeture IMAP
			print ("deconnecter du serveur")
			imaplib.IMAP4.close
			imaplib.IMAP4.logout
		
	except IOError:
		i01.speakBlocking("le serveur est hors service")
	except OSError:
		i01.speakBlocking("oups il y a une erreur")
	except ValueError:
		i01.speakBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

def photoa(destinataire):
	try:
		#i01.speakBlocking(destinataire)
		print ("destinataire : " + destinataire)
		# creation d un dictionnaire des amis
		dico = {"jean pierre":"son adresse mail" , "colette":"son adresse mail"}
		# message si pas trouver
		if (dico.get(destinataire) == None):
			print("Amis inconnu dans l annuaire")
			i01.speakBlocking("personne inconnu au bataillon")
		else:
			print ("adresse mail : " + dico.get(destinataire))
			#i01.speakBlocking(" fais parti de tes amis  regarde moi dans les yeux")
   
			# creation du service open cv et parametrage
			i01 = runtime.start('i01','InMoov2')
			cv = i01.startPeer('opencv')
			cv.addFilter("pdown","PyramidDown")
			cv.setDisplayFilter("pdown")
			cv.setCameraIndex(0)
			cv.capture()
			i01.speakBlocking("regarde moi bien dans les yeux , le petit oiseau va sortir")
			#ajouter le fichier click.mp3 dans ../data/sound
			#AudioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
			AudioPlayer.playFile('data/sounds/click.mp3')
			#sauve image dans data/OpenCV
			#photoFileName = cv.saveImage() 
			photoFileName = i01_opencv.recordFrame()
			#photoFileName = i01.opencv.recordSingleFrame()
			print(photoFileName)
   
			sleep(2) 
			cv.removeFilter('pdown') # supprime le filtre
			cv.stopCapture() # arrete capture
   
			i01.speakBlocking("merci la photo est enregistrer  Envoi de la photo a " + destinataire)
			sleep(2)
   
			# ici envoi du mail avec piece jointe
			fromaddr = "mail expediteur"
			toaddr = (dico.get(destinataire))
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = "photo souvenir"
			body = "tu a une photo en attente"
			msg.attach(MIMEText(body, 'multipart/mixed'))
   
   			# filname nom du fichier [13:]
			#filename = photoFileName
			
			filename = "image.png"
			attachement = open("c:/mrl/myrobotlab-1.1.1050/data/opencv/image.png"  ,"rb")
			print("Nom du Fichier : "+ filename)
			#attachement = open(photoFileName,'rb')
			print(attachement)
            #encodage du mail      
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachement).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
			msg.attach(part)
			# valeur du serveur smtp securise ou pas
			#server = smtplib.SMTP('smtp.gmail.com', 587)
			server = smtplib.SMTP('smtp-msa.orange.fr', 587)
			#server.starttls()
			#server.login(fromaddr, "/xxxxxx")
			server.login(fromaddr, "YOUR PASSWORD MAIL")
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
   
			
			i01.speakBlocking("photo transmis a " + destinataire)
			sleep(100)
			server.quit()
			server.close()

	except IOError:
		i01.speakBlocking("le serveur est hors service  mail non transmis")
