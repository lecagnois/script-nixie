# -- coding: utf-8 --
import imaplib
import email
from email.header import decode_header
from HTMLParser import HTMLParser  # Pour parser le HTML

# Charge adresse mailde votre compte et password dans service security
security.loadStore()
expediteur =  security.getSecret("mailsender")
password = security.getSecret("mailpassword")
mail_serveur = 'imap.orange.fr'
mail_port = 993  # Port SSL

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
                    flag=1
                    # Connexion au serveur IMAP
                    mail = imaplib.IMAP4_SSL(mail_serveur, mail_port)
                    mail.login(expediteur, password)
                    print("Connection du serveur IMAP")
                    # Sélection de la boîte de réception
                    mail.select('inbox')
                    cpt=0  # compteur de nb de messages
                    # Recherche des e-mails 
                    _, data = mail.search(None, '( FROM "' + ligne[6] + '")') # Récupérer tous les emails

                   # Si des e-mails sont trouvés
                    if data[0]:
                        email_ids = data[0].split()
                        # Calcul du nombre d'e-mails trouvés
                        num_emails = len(email_ids)
                        i01.speakBlocking(u"J'ai trouvé " +str(num_emails) + " message de "+ destinataire)
                        for email_id in email_ids:
                            _, data = mail.fetch(email_id, '(RFC822)')
                            msg = email.message_from_string(data[0][1])
                            # Décoder l'expéditeur et le sujet (gestion de l'encodage)
                            #expediteur2 = decode_header(msg['From'])[0][0]
                            sujet = decode_header(msg['Subject'])[0][0]
                            contenu_html = ""
                            contenu_texte = ""
                            # contenu format texte
                            for part in msg.walk():
                                if part.get_content_type() == 'text/plain':
                                    payload = part.get_payload(decode=True)
                                    if payload:
                                        charset = part.get_content_charset()
                                        if charset:
                                            try:
                                                contenu_texte += payload.decode('utf-8', errors='replace')
                                                contenu_texte.replace(u'Ã©',u'é') # pour les accents
                                            except:
                                                contenu_texte += "Erreur de décodage texte"
                                        else:
                                            contenu_texte += "Pas de charset spécifié pour la partie texte"
                                    cpt=cpt+1
                                            
                            #contenu format html
                                elif part.get_content_type() == 'text/html':
                                    payload = part.get_payload(decode=True)
                                    if payload:
                                        charset = part.get_content_charset()
                                        if charset:
                                            try:
                                                html = payload.decode(charset, errors='replace')
                                                html = html.replace(u'&#233;',u'é') # pour les accents
                                                contenu_html += strip_tags(html)  # Supprimer les balises HTML
                                            except:
                                                contenu_html += "Erreur de décodage HTML"
                                        else:
                                            contenu_html += "Pas de charset spécifié pour la partie HTML"
                                    cpt=cpt+1
                            if cpt == 0 :
                                cpt=1
                                
                            # resultats des informations contenu limité a 100 caracteres
                            #i01.speakBlocking(u"Expéditeur:"+ expediteur2.decode('utf-8',errors='replace'))
                            i01.speakBlocking(u"Message " + str(cpt))
                            i01.speakBlocking(u"Sujet du message : " + sujet.decode('utf-8',errors='ignore'))
                            if (len(contenu_texte)) > 2 :
                                i01.speakBlocking(u"Contenu du message TEXTE : " + contenu_texte[:100])
                            if (len(contenu_html)) > 2 and (len(contenu_texte)) <1 :
                                i01.speakBlocking(u"Contenu du message HTML : "+ contenu_html[:100])
                    else:
                        i01.speakBlocking(u"Je n'est pas trouvé de message de,"+ destinataire)
                    #fermeture IMAP
                    print("deconnecter du serveur IMAP")
                    mail.close()
                    mail.logout()
                    
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
        
# Classe pour parser le HTML (extrait le texte)
class MLStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()