# -- coding: utf-8 --

def loto(phrase,the,chance,fin,nb_boules_principales, nb_tirages_principaux, nb_boules_complementaires) :
    table1 = []
    date = time.strftime('%d-%B-%Y')  # variable du jour format (JJ-MM-AAAA)
    # Tirage aléatoire et tri des numéros principaux
    numeros_principaux = sorted(random.sample(range(1, nb_boules_principales + 1), nb_tirages_principaux))
    # Tirage aléatoire du numéro complémentaire
    complementaire = random.randint(1, nb_boules_complementaires)
    
    # Affichage des numéros un par et aliment table1 pour le fichier loto.csv
    i01.speakBlocking(phrase)
    for numero in numeros_principaux:
        #print(numero)
        i01.speakBlocking(the+str(numero))
        table1.append(numero) 
           
    table1.append(complementaire)
    print(table1)
    i01.speakBlocking(chance)
    i01.speakBlocking(str(complementaire))
   
    # vérification si existe fichier loto.csv si oui on ajoute numeros 
    if os.path.exists('data/loto.csv'):
        valeurs = [[str(table1[0]),str(table1[1]),str(table1[2]),str(table1[3]),str(table1[4]),str(table1[5]),date]]
        f = open('data/loto.csv', 'a')
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
    else :
    # si non creation du fichier historique du tirage 
        entetes = [u'NUMERO 1',u'NUMERO 2',u'NUMERO 3',u'NUMERO 4',u'NUMERO 5',u'COMPLEMENTAIRE',u'DATE']
        valeurs = [[str(table1[0]),str(table1[1]),str(table1[2]),str(table1[3]),str(table1[4]),str(table1[5]),date]]
        f = open('data/loto.csv', 'w')
        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)
        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
        f.close()
        
    i01.speakBlocking(fin)


