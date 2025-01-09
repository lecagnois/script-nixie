# -- coding: utf-8 --

# Charge expediteur et password dans service security
security.loadStore()
expediteur =  security.getSecret("mailsender")
password = security.getSecret("mailpassword")
serveurimap = "imap.orange.fr"



def mailsend(amis,message):
  #Cherche ton amis dans le fichier Bdamis.csv et envoi un mail a son adresse  
    if password == None:
        i01_chatBot.getResponse("PASSWORD_KO")
    else:
        try:
            # si base de donnees existe on cherche son ami
            if os.path.exists('data/bdamis.csv'):
                flag = 0
                f = open('data/bdamis.csv', 'r')
                # lecture du fichier CSV.
                reader = csv.reader(f,delimiter=";")
                # Boucle lecture lignes une par une colonne 0 (champ nom).
                for ligne in reader:
                    if (amis == ligne[0]):
                        flag=1
                        #i01.speakBlocking( amis + " fais parti de tes amis ")
                        i01_chatBot.getResponse("AMIS_OK")
                        #print(amis + " fais parti de tes amis ")
                        message = message.strip("Si ok")[:-22]
                        envoyer_email_texte(message,ligne[5]) # champ adresse dans bd
                f.close()
                if flag==0 :
                    i01_chatBot.getResponse("AMIS_KO")
            else : 
                # le fichier bdamis n existe pas
                i01_chatBot.getResponse("ANNUAIRE_KO")     
        except IOError as e:
            print("le serveur est hors service , mail non transmis",e)
        except OSError as e:
            print("oups il y a une erreur",e)
        except ValueError as e :
            print("oups il y a une erreur ",e)


def envoyer_email_texte(corps, destinataire):
	try:
		# Création du message
		server = smtplib.SMTP("smtp.orange.fr", 587)
		server.starttls()
		server.login(expediteur, password)
		msg = MIMEMultipart()
		msg['From'] = expediteur
		msg['To'] = destinataire
		msg['Subject'] = "Envoi de InMoov"
		msg.attach(MIMEText(corps, 'plain' , 'utf-8'))
		server.sendmail(expediteur, destinataire, msg.as_string())
		server.quit()
		i01_chatBot.getResponse("EMAIL_OK")
	except Exception as e:
		i01_chatBot.getResponse("EMAIL_KO")
		print("Erreur : ",e)
	except smtplib.SMTPServerDisconnected as e:
		print("Erreur : ", e)

def liremail(destinataire):
	try :
		# si base de donnees existe
		if os.path.exists('data/bdamis.csv'):
			flag=0
			f = open('data/bdamis.csv', 'r')
       		# lecture du fichier bdamis.CSV
			reader = csv.reader(f,delimiter=";")
	    	# Boucle lecture lignes une par une colonne 0 (champ nom).
			for ligne in reader:
				if (destinataire == ligne[0] and ligne[5] != ""):
					flag = 1
					mail = imaplib.IMAP4_SSL(serveurimap)
					# imaplib module implements connection based sur protocol IMAPv4 
					mail.login(expediteur, password)
					mail.list() 
					mail.select('inbox') # Connecter a inbox.
					(status,nbMessages) = mail.select('INBOX')
					print("connecter inbox")				
					#Rechercher message dans expediteur
					result, data = mail.uid('search', None, '(FROM "'+ligne[6]+'")')
					i = len(data[0].split()) # data[0] supprime espace
					Totalmsg = re.findall('\d+', str(nbMessages))[0]
					print (result + ' Nombre de messages = ' + str(Totalmsg))
					i01.speakBlocking(u"il y a  au total "+str(Totalmsg)+ " messages dans ta boite mail ")
					print("trouver : " +str(i))
					i01.speakBlocking(u"j'ai trouvé " + str(i) + " message de " + destinataire )
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
								i01.speakBlocking(u"message " + str(x+1) +". "+ Mreponse)
							if part.get_content_type() == "multipart/mixed" : # ignore piece jointe
								body = part.get_payload(decode=False)
							else:
								continue				
					if i == 0 :
						print("pas de messages")
						i01_chatBot.getResponse("LIREMAIL_BYE")				
					#fermeture IMAP
					print ("deconnecter du serveur")
					imaplib.IMAP4.close
					imaplib.IMAP4.logout
			if flag == 0 :
			    # message si pas trouver dans l annuaire
				i01_chatBot.getResponse("AMIS_KO_BIS")	    
		else : # la bd des amis n existe pas
			i01_chatBot.getResponse("ANNUAIRE_KO")
	except IOError as e:
		i01_chatBot.getResponse("EMAIL_KO")
		print(e)
	except OSError as e:
		print("oups il y a une erreur",e)
	except ValueError as e:
		print("oups il y a une erreur ",e)

# pour envoyer des images ne fonction que avec python 3 a revoir
def envoyer_image(destinataire, image_path):
	#envoyer_image("xxxx@xxx.fr", "data/opencv/jp.png")
    try:
        # Création du message
        message = MIMEMultipart()
        message['From'] = expediteur
        message['To'] = destinataire
        message['Subject'] = 'Image jointe'
        # Corps du message
        body = "Voici l'image que je vous envoie."
        message.attach(MIMEText(body, 'plain'))
        # Ajout de l'image
        with open(image_path, 'rb') as f:
            img_data = f.read()
            image = MIMEImage(img_data, name=os.path.basename(image_path))
            message.attach(image)
        # Connexion au serveur SMTP et envoi du message
        with smtplib.SMTP(serveursmtp, port) as server:
            server.starttls()
            server.login(expediteur, password)
            text = message.as_string()
            server.sendmail(expediteur, destinataire, text)
            i01.speakBlocking(u"Photo envoyé a : " + destinataire)
    except Exception as e:
        i01_chatBot.getResponse("EMAIL_KO")
