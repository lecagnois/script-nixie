# -- coding: utf-8 --
def imagephoto(image) :
    # si open cv deja lancer
    if runtime.isStarted('i01.opencv') and runtime.isStarted('i01.mouth.audioFile'):
        if image =="droite":
            i01.setHeadSpeed(22.0, 22.0)
            i01.moveHead(180,90)
            i01.finishedGesture()
        if image =="gauche":
            i01.setHeadSpeed(22.0, 22.0)
            i01.moveHead(90,180)
            i01.finishedGesture()	
        if image =="centre":
            i01.setHeadSpeed(22.0, 22.0)
            i01.moveHead(90,100)
            i01.finishedGesture()
        audioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')
        i01.speakBlocking(u"regarde moi bien dans les yeux , le petit oiseau va sortir")
        audioPlayer.playFile('data/sounds/click.mp3')
        cv = i01.startPeer('opencv')
        cv.addFilter("pdown","PyramidDown")
        cv.setDisplayFilter("pdown")
        cv.setCameraIndex(0)
        cv.setGrabberType("VideoInput")
        cv.capture()
        sleep(2)
        cv.saveImage()
        cv.removeFilter('pdown') # supprime le filtre
        cv.stopCapture() # arrete capture
        i01.speakBlocking(u"j'ai enregistré la photo dans ma memoire")
    else:
        i01_chatBot.getResponse("YEUX_OFF") # Response dans A_email.aiml


def photoa(amis):
    # si openCV deja lancer
    if runtime.isStarted('i01.opencv') and runtime.isStarted('i01.mouth.audioFile'):
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
                        i01_chatBot.getResponse("AMIS_OK_PHOTO") # Response dans A_email.aiml
                        cv = i01.startPeer('opencv')
                        email = runtime.start('email', 'Email')
                        cv.capture()
                        sleep(2)
                        picture_file = cv.recordFrame()
                        cv.saveImage()
                        print("je sauve l image")
                        cv.stopCapture() # stop capture
                        #envoyer_image avec le service email.sendEmail(mail destinataire,sujet,body,image) # champ adresse dans bd
                        email.sendEmail(ligne[5], 'mail de inmoov ' , amis +' voici la photo d\'un amis ', picture_file)
                f.close()
                if flag==0 :
                    i01_chatBot.getResponse("AMIS_KO") # votre ami n existe pas dans bdamis
            else :
                i01_chatBot.getResponse("ANNUAIRE_KO") # le fichier bdamis n existe pas
        except IOError as e:
            print("le serveur est hors service , mail non transmis",e)
        except OSError as e:
            print("oups il y a une erreur",e)
        except ValueError as e :
            print("oups il y a une erreur ",e)
    else:
        i01_chatBot.getResponse("YEUX_OFF") # Response dans A_email.aiml
      


