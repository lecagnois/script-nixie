# -- coding: utf-8 --

def tirage():
    try :
        annee = (time.strftime('%Y'))
        page= urllib.urlopen('http://loto.akroweb.fr/loto-historique-tirages') 
        html = page.read()
        # suppresion des balises avec transformation byte en chaine unicode
        tirage = html[21000:30000].decode('utf-8')
        tirage=tirage.replace('width=\"210\"','').replace('\t','').replace('\r','').replace("<td width=\"210\">","").replace("<td width=\"90\">","").replace("<td width=\"100\">","").replace("</td>","").replace("</td","").replace("<td width=\"100\" class=\"font-blue\">","")
        # print (tirage)
        # transforme la chaine en list
        resultat = (tirage.split())
        #print(resultat)
        #recherche index annee dans la liste resultat pour trouver les numéros
        pos=(resultat.index(annee))
        i01.speakBlocking(u"voici les numéros du dernier tirage du loto")
        i01.speakBlocking ('le : ' + resultat[pos+1])
        i01.speakBlocking ('le : ' + resultat[pos+2])
        i01.speakBlocking ('le : ' + resultat[pos+3])
        i01.speakBlocking ('le : ' + resultat[pos+4])
        i01.speakBlocking ('le : ' + resultat[pos+5])
        print("Tirage = "+resultat[pos+1]+"-"+resultat[pos+2]+"-"+resultat[pos+3]+"-"+resultat[pos+4]+"-"+resultat[pos+5])
        if (len(resultat[pos+6])==5) :
            i01.speakBlocking (u'et le complémentaire est le : '+ resultat[pos+6][:1])
            print (u'et le complémentaire est le : '+ resultat[pos+6][:1])
        else:
            i01.speakBlocking (u'et le complémentaire est le : '+ resultat[pos+6][:2])
            print (u'et le complémentaire est le : '+ resultat[pos+6][:1])
        # comparaison avec la BBD loto
        if os.path.exists('data/loto.csv'):
            f = open('data/loto.csv', 'r')
            reader = csv.reader(f,delimiter=";")
            for col in reader:
                dernier = (col[0:7])
            f.close()
            cpt = 0
            if (dernier[0] == resultat[pos+1]) :
                cpt = cpt+1
            if (dernier[1] == resultat[pos+2]) :
                cpt = cpt+1
            if (dernier[2] == resultat[pos+3]) :
                cpt = cpt+1   
            if (dernier[3] == resultat[pos+4]) :
                cpt = cpt+1   
            if (dernier[4] == resultat[pos+5]) :
                cpt = cpt+1
            if (dernier[5] == resultat[pos+6][:1]) :
                cpt = cpt+1
            if cpt >= 1 :
                i01.speakBlocking (u"j'avais trouvé " + str(cpt) + u"bons numéros , j'espère que tu a joué mon tirage")
            if cpt == 0 :
                i01.speakBlocking (u"désolé tu n'a aucun bon numéro ")
 
    except IOError:
        i01.speakBlocking(u"le serveur est hors service")
    except ValueError:
        i01.speakBlocking(u"oups il y a une erreur de valeur ")
    except:
        print(sys.exc_info()[0])
        raise