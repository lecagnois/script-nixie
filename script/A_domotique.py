# -- coding: utf-8 --
import csv
import os
import urllib
import socket


adresseip = "192.168.1.30:8081"
ipsocket ="192.168.1.30"
port = 8081

def bddomotique(nom,id):  
    # si fichier bddomotique existe  
    if os.path.exists('data/bddomotique.csv'):
        
        #verification doublon
        flag = 0
        f = open('data/bddomotique.csv', 'r')
        # Creation du lecteur CSV.
        reader = csv.reader(f,delimiter=";")
	    # Boucle lecture lignes une par une colonne 0.
        for ligne in reader:
           
            if (nom.upper() == ligne[0]):
                i01.speakBlocking(u"j'ai déjà un terminal nonmé "+ nom + u" je ne peux pas l'ajouter")
                flag = 1
        f.close()
        #ajout des donnees si nom inexistant   
        if flag == 0 :
            valeurs = [[nom.upper(),id]]
            f = open('data/bddomotique.csv', 'a')
            for valeur in valeurs:
                ligne = ";".join(valeur) + "\n"
                f.write(ligne)
            f.close()
            i01.speakBlocking(u"J'ai ajouté le terminal nonmé : " + nom + u" a la base de données")  
                
    else:
        #création du fichier bddomotique
        entetes = [u'NOM',u'ID']
        valeurs = [[nom.upper(),id]]
        f = open('data/bddomotique.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
        i01.speakBlocking(u"J'ai ajouté le terminal nommé " +nom+ u" a la base de données")  
        
def domoAllume(terminal):
    try:
        # verifier si serveur actif
        #i01.speakBlocking(u"je vérifie si le serveur domotique est allumé" )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipsocket, port))
        # si fichier bddomotique existe  
        if os.path.exists('data/bddomotique.csv'):
            # ouverture et lecture de la BD
            flag = 0
            f = open('data/bddomotique.csv', 'r')
            reader = csv.reader(f,delimiter=";")
	        # Boucle lecture lignes une par une colonne 0.
            for ligne in reader:
                
                if (terminal.upper() == ligne[0] and ligne[1] != ""):
                    #//192.168.1.30:8081/json.htm?type=command&param=switchlight&idx=68&switchcmd=On
                    #//on /off    /json.htm?type=command&param=switchlight&idx=99&switchcmd=Toggle
                    url='http://'+adresseip+'/json.htm?type=command&param=switchlight&idx='+ligne[1]+'&switchcmd=On' 
                    urllib.urlopen(url)
                    i01.speakBlocking(u"commande validée")
                    flag=1
            f.close()
            if flag==0:
                i01.speakBlocking(terminal + u" n'existe pas comme terminal dans ma base domotique ou l'idx est erroné" )
     
        else:  # la bd des amis n existe pas
            i01.speakBlocking(u"tu dois d'abord créer ta base de données domotique . Dis DOMOTIQUE pour le créer")
         
    except socket.error:
        i01.speakBlocking(u"le serveur domotique est hors service ")
    except ValueError:
        i01.speakBlocking("oups il y a une erreur ")
    except:
        print(sys.exc_info()[0])
        raise
    
    
def domoEteint(terminal):
    try:
        # verifier si serveur actif
        #i01.speakBlocking(u"je vérifie si le serveur domotique est allumé" )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipsocket, port))
        # si fichier bddomotique existe  
        if os.path.exists('data/bddomotique.csv'):
            # ouverture et lecture de la BD
            flag = 0
            f = open('data/bddomotique.csv', 'r')
            reader = csv.reader(f,delimiter=";")
	        # Boucle lecture lignes une par une colonne 0.
            for ligne in reader:
                
                if (terminal.upper() == ligne[0] and ligne[1] != ""):
                    #//192.168.1.30:8081/json.htm?type=command&param=switchlight&idx=68&switchcmd=On
                    #//on /off    /json.htm?type=command&param=switchlight&idx=99&switchcmd=Toggle
                    url='http://'+adresseip+'/json.htm?type=command&param=switchlight&idx='+ligne[1]+'&switchcmd=Off' 
                    urllib.urlopen(url)
                    i01.speakBlocking(u"commande validée")
                    flag=1
            f.close()
            if flag==0:
                i01.speakBlocking(terminal + u" n'existe pas comme terminal dans ma base domotique ou l'idx est erroné" )
     
        else:  # la bd des amis n existe pas
            i01.speakBlocking(u"tu dois d'abord créer ta base de données domotique . Dis DOMOTIQUE pour le créer")
         
    except socket.error:
        i01.speakBlocking(u"le serveur domotique est hors service ")
    except ValueError:
        i01.speakBlocking("oups il y a une erreur ")
    except:
        print(sys.exc_info()[0])
        raise
    
def domoTemperature(terminal):
    try:
        # verifier si serveur actif
        #i01.speakBlocking(u"je vérifie si le serveur domotique est allumé" )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipsocket, port))
        # si fichier bddomotique existe  
        if os.path.exists('data/bddomotique.csv'):
            # ouverture et lecture de la BD
            flag = 0
            f = open('data/bddomotique.csv', 'r')
            reader = csv.reader(f,delimiter=";")
	        # Boucle lecture lignes une par une colonne 0.
            for ligne in reader:
                #print(terminal)
                if (terminal.upper() == ligne[0] and ligne[1] != ""):
                    #//192.168.1.30:8081/json.htm?type=devices&rid=107
                    url=urllib.urlopen('http://'+adresseip+'/json.htm?type=devices&rid='+ligne[1])
                    req = url.read()
                    tableau = req[1:2000].split('"')
                    Mtemperature = []
                    #print(tableau)
                    # remplissage du tableau champ temp 
                    i=0
                    while i < len(tableau):
                        if (tableau[i]=='Temp'):
                            Mtemperature.append(tableau[i+1])
                        i=i+1	
                    
                    print(u"la température est de : "+ str((Mtemperature[0][3:7])) + u" degré")
                    i01.speakBlocking(u"la température est de : "+ str((Mtemperature[0][3:7])) + u" degré")
                    
                    flag=1
                    
            f.close()
                      
            if flag==0:
                i01.speakBlocking(terminal + u" n'existe pas comme terminal dans ma base domotique ou l'idx est erroné" )
     
        else:  # la bd des amis n existe pas
            i01.speakBlocking(u"tu dois d'abord créer ta base de données domotique . Dis DOMOTIQUE pour le créer")
         
    except socket.error:
        i01.speakBlocking(u"le serveur domotique est hors service ")
    except ValueError:
        i01.speakBlocking("oups il y a une erreur ")
    except:
        print(sys.exc_info()[0])
        raise
    

