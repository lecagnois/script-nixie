# -- coding: utf-8 --
import random
import os

def loto(phrase,the,chance,fin) :
    table1  = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
    tablefin = []
    doublon = []
    date = time.strftime('%d-%B-%Y')  # variable du jour format (17-01-2023)
    #ear.setAutoListen(False)
    #stopListening()
    for i in table1:
        if i not in tablefin:
            tablefin.append(i) #supprime les doublons
        else:
            doublon.append(i) #extraire les doublons
    d = len(doublon)
    while d > 0:
        #nouveau tirage
        doublon = []
        table1  = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
        # recherche doublon
        for i in table1:
            if i not in tablefin:
                tablefin.append(i) #supprime les doublons
            else:
                doublon.append(i) #extraire les doublons
                # si il existe doublon d+1 et vite la table
            if (len(doublon)==1)or(len(doublon)==2)or(len(doublon)==3)or(len(doublon)==4)or(len(doublon)==5):
                i01.speakBlocking(u"j'ai trouvé un doublon , je refais un tirage")
                d = d+1
                doublon =[]
            else:
                d = 0
            break
    # tri la table avant de la dire sauf complementaire
    table1.sort()
    i01.speakBlocking(phrase)
    i01.speakBlocking(the+str(table1[0]))
    i01.speakBlocking(the+str(table1[1]))
    i01.speakBlocking(the+str(table1[2]))
    i01.speakBlocking(the+str(table1[3]))
    i01.speakBlocking(the+str(table1[4]))
    compl = str((random.randint(1,10)))
    i01.speakBlocking(chance+compl)
    i01.speakBlocking(fin)
     
    # vérification si existe fichier sav loto si oui on ajoute numeros
    if os.path.exists('data/loto.csv'):
        valeurs = [[str(table1[0]),str(table1[1]),str(table1[2]),str(table1[3]),str(table1[4]),compl,date]]
        f = open('data/loto.csv', 'a')
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
    
    else :
    # si non creation du fichier historique du tirage 
        entetes = [u'NUMERO 1',u'NUMERO 2',u'NUMERO 3',u'NUMERO 4',u'NUMERO 5',u'COMPLEMENTAIRE',u'DATE']
        valeurs = [[str(table1[0]),str(table1[1]),str(table1[2]),str(table1[3]),str(table1[4]),compl,date]]
        f = open('data/loto.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()

