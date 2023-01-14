import locale

def anniversaire():
    #date en francais
    locale.setlocale(locale.LC_TIME,'')
    i01.speakBlocking(time.strftime('Nous sommes le %A %d %B %Y,',time.localtime()))

    # la clef du dico sera la date systeme
    anniversaire = time.strftime('%m-%d')
    jour = int(time.strftime('%d'))
    mois = int(time.strftime('%m'))
    annee = int(time.strftime('%Y'))
     
    # creation d un dictionnaire anniversaire entrer ici vos parents et amis (index mois-jour : donnees)
    dico = {"11-21":"orélie 1974" ,"03-06":"jean-pierre 1958" ,"03-14":"francis 1961" , "11-25":"colette 1948" , "01-06": "JARVIS 2014"}	
    # creation du dictionnaire des saints index sur date la date
    saint = {
    "11-01":"la tousaint","11-02":"les victorin","11-03":"les hubert","11-04":"les charles","11-05":"les sylvie","11-06":"les leonard","11-07":"les Carine","11-08":" les geoffroy","11-09":"les theodore","11-10":"les laion","11-11":"l armistice 1918","11-12":"les christian","11-13":"les brice","11-14":"les sidoine","11-15":"les albert","11-16":"les marguerite","11-17":"les elisabeth","11-18":"les aude","11-19":"les tanguy","11-20":"les edmond","11-21":"les gelace","11-22":"les cecile","11-23":"les clement","11-24":"les flora","11-25":"les catherine","11-26":"les delphine","11-27":"les severin","11-28":"les jacques","11-29":"les saturnin","11-30":"les andrai",
    "12-01":"les florence ","12-02":"les viviane","12-03":"les francois xavier","12-04":"les barbara","12-05":"les geralde","12-06":"les nicola","12-07":"les ambroise","12-08":" les elfried","12-09":"les pierre fourrier","12-10":"les romaric","12-11":"les daniel","12-12":"les corentin","12-13":"les lucie","12-14":"les odile","12-15":"les ninon","12-16":"les alice","12-17":"les gael","12-18":"les gatien","12-19":"les urbain","12-20":"les theophine","12-21":"les pierre canisius","12-22":"les francoise xaviere","12-23":"les armand","12-24":"les adele","12-25":"les noel","12-26":"les etienne","12-27":"les jean apotre","12-28":"les innocent","12-29":"les david","12-30":"les roger","12-31":"les sylvestre",
    "01-01":"le jour de l an ","01-02":"les basile ","01-03":"les genevieve","01-04":"les odilon","01-05":"les edouard ","01-06":"les melaine","01-07":"les raymond","01-08":" les lucien","01-09":"les alix","01-10":"les guillaume","01-11":"les paulin","01-12":"les tatiana","01-13":"les yvette","01-14":"les nina","01-15":"les remi","01-16":"les marcel","01-17":"les roseline","01-18":"les prisca","01-19":"les marius ","01-20":"les sebastien","01-21":"les agnes","01-22":"les vincent","01-23":"les emerence ","01-24":"les francois","01-25":"les ananie","01-26":"les paules ","01-27":"les angele","01-28":"les thomas","01-29":"les gildas","01-30":"les martine","01-31":"les marcelle",
    "02-01":"les ella ","02-02":"les theophane","02-03":"les blaise","02-04":"les veronique","02-05":"les agathe","02-06":"les gaston","02-07":"les eugenie","02-08":" les jacqueline","02-09":"les apolline","02-10":"les armaud","02-11":"les heloise","02-12":"les felix","02-13":"les beatrice","02-14":"les valentin","02-15":"les claude","02-16":"les julienne","02-17":"les alexis","02-18":"les nadine","02-19":"les gabin","02-20":"les aimee","02-21":"les enora ","02-22":"les isabelle","02-23":"les lazare","02-24":"les modeste","02-25":"les romeo","02-26":"les nestor","02-27":"les honorine","02-28":"les romain","02-29":"les auguste",
    "03-01":"les aubin","03-02":"les charles","03-03":"les guenole","03-04":"les casimir","03-05":"les olive","03-06":"les colette","03-07":"les felicite","03-08":" les ryan","03-09":"les francoise","03-10":"les vivien","03-11":"les rosine","03-12":"les justine","03-13":"les rodrigue","03-14":"les mathilde","03-15":"les louise","03-16":"les benedicte","03-17":"les patrice","03-18":"les cyrile","03-19":"les joseph","03-20":"les herbert","03-21":"les clemence","03-22":"les lea","03-23":"les victorien","03-24":"les catherine","03-25":"les humbert","03-26":"les larissa","03-27":"les habib","03-28":"les gontran","03-29":"les gladys","03-30":"les amaidai","03-31":"les benjamin",
    "04-01":"les hugue","04-02":"les sandrine","04-03":"les richard","04-04":"les isodore","04-05":"les iraine","04-06":"les marcelin","04-07":"les jean baptiste","04-08":" les julie","04-09":"les gautier","04-10":"les terence","04-11":"les stanislas","04-12":"les jules","04-13":"les ida","04-14":"les maxime","04-15":"les paterne","04-16":"les laionide","04-17":"les anicet","04-18":"les parfait","04-19":"les emma","04-20":"les odette","04-21":"les anselme","04-22":"les alexandre","04-23":"les georges","04-24":"les fidele","04-25":"les marc","04-26":"les alda","04-27":"les zita","04-28":"les valairie","04-29":"les catherine","04-30":"les robert",
    "05-01":"les jairaimy","05-02":"les boris","05-03":"les philippe","05-04":"les sylvain","05-05":"les judith","05-06":"les prudence","05-07":"les gisaile","05-08":"les daisirai","05-09":"les pacome","05-10":"les solveig","05-11":"les estelle","05-12":"les achille","05-13":"les fatima","05-14":"les mathias","05-15":"les denise","05-16":"les honorai","05-17":"les pascal","05-18":"les eric","05-19":"les yves","05-20":"les lydie","05-21":"les constantin","05-22":"les emile","05-23":"les didier","05-24":"les donatien","05-25":"les sofia","05-26":"les bairengere","05-27":"les augustin","05-28":"les germain","05-29":"les gairaldine","05-30":"les johanna","05-31":"les maelys",
    "06-01":"les justin","06-02":"les blandine","06-03":"les kevin","06-04":"les clothilde","06-05":"les igor","06-06":"les norbert","06-07":"les gilbert","06-08":"les maidart","06-09":"les diane","06-10":"les landry","06-11":"les barnabai","06-12":"les guy","06-13":"les antoine","06-14":"les elise","06-15":"les germaine","06-16":"les raigis","06-17":"les hervai","06-18":"les laionce","06-19":"les romualde","06-20":"les silvere","06-21":"les gonzague","06-22":"les alban","06-23":"les audrey","06-24":"les jean baptiste","06-25":"les prosper","06-26":"les thelma","06-27":"les cyrielle","06-28":"les irainai","06-29":"les paul","06-30":"les martial",
    "07-01":"les thierry","07-02":"les colomban","07-03":"les thomas","07-04":"les florent","07-05":"les zoai","07-06":"les nolwen","07-07":"les raoul","07-08":"les thibault","07-09":"les amandine","07-10":"les amalia","07-11":"les benoit","07-12":"les olivier","07-13":"les henri","07-14":"les camille","07-15":"les vladimir","07-16":"les carmen","07-17":"les charlotte","07-18":"les fraidairic","07-19":"les ornella","07-20":"les marina","07-21":"les victor","07-22":"les madeleine","07-23":"les brigitte","07-24":"les christine","07-25":"les jacques","07-26":"les anne","07-27":"les nathalie","07-28":"les samson","07-29":"les marthe","07-30":"les juliette","07-31":"les ignace",
    "08-01":"les alphonse","08-02":"les julien","08-03":"les lydie","08-04":"les violette","08-05":"les abel","08-06":"les octavien","08-07":"les gaetan","08-08":"les dominique","08-09":"les tara","08-10":"les laurent","08-11":"les claire","08-12":"les clarisse","08-13":"les hippolyte","08-14":"les evrard","08-15":"les marie","08-16":"les armel","08-17":"les janis","08-18":"les hailene","08-19":"les eudeline","08-20":"les bernard","08-21":"les grace","08-22":"les fabrice","08-23":"les rose","08-24":"les barthailaimy","08-25":"les louis","08-26":"les natacha","08-27":"les monique","08-28":"les augustin","08-29":"les sabine","08-30":"les fantine","08-31":"les aristide",
    "09-01":"les gilles","09-02":"les ingrid","09-03":"les graigoire","09-04":"les rosalie","09-05":"les raissa","09-06":"les bertrand","09-07":"les reine","09-08":"les adrien","09-09":"les alain","09-10":"les ines","09-11":"les vinciane","09-12":"les apolinaire","09-13":"les aziz","09-14":"les cyprien ","09-15":"les dolores","09-16":"les edith","09-17":"les renaud","09-18":"les nadege","09-19":"les aimilie","09-20":"les ysoline","09-21":"les matthieu","09-22":"les sylvain","09-23":"les constant","09-24":"les silouane","09-25":"les solene","09-26":"les damien","09-27":"les vincent","09-28":"les lucas","09-29":"les gabriel","09-30":"les jairome",
    "10-01":"les tess","10-02":"les laiger","10-03":"les gairard","10-04":"les francois","10-05":"les fleur","10-06":"les bruno","10-07":"les serge","10-08":"les pailagie","10-09":"les denis","10-10":"les ghislain","10-11":"les firmin","10-12":"les wilfried","10-13":"les edouard","10-14":"les juste","10-15":"les thairese","10-16":"les edwige","10-17":"les baudouin","10-18":"les luc","10-19":"les renai","10-20":"les adeline","10-21":"les sailine","10-22":"les ailodie","10-23":"les elphie","10-24":"les florentin","10-25":"les daria","10-26":"les saidric","10-27":"les aimeline","10-28":"les dimitri","10-29":"les jude","10-30":"les ma aiva","10-31":"les quentin"
            }

	# mise en forme des dates
	
    madate= datetime.now()
    rappel = str(int(str((madate))[5:7]))+"-"+str((int(str((madate))[8:11])+7))
    rappel2 = str(int(str((madate))[5:7]))+"-"+str((int(str((madate))[8:11])+1))
    sleep(2)

    if (dico.get(rappel) != None):
        agedico = int(dico.get(rappel)[-4:])
        prenom = (dico.get(rappel)[:-4])
        age = annee - agedico 
        i01.speakBlocking(u"c'est l'anniversaire de " + prenom + str(age) +" ans dans 7 jours")

    if (dico.get(rappel2) != None):
        agedico = int(dico.get(rappel2)[-4:])
        prenom = (dico.get(rappel2)[:-4])
        age = annee - agedico 
        i01.speakBlocking(u"demain c'est l'anniversaire de " + prenom + str(age) +" ans")

    if (dico.get(anniversaire) != None):
        agedico = int(dico.get(anniversaire)[-4:])
        prenom = (dico.get(anniversaire)[:-4])
        age = annee - agedico 
        i01.speakBlocking("bon anniversaire " + prenom + str(age) +" printemps ,tu ne les fais pas")
		#i01.speakBlocking("WHAAAAA . bon anniversaire , " + prenom +" tu est en bonne forme , Pour une quadragénaire , plein de bisous")
    # si pas anniversaire on faite les saints 
    if ((dico.get(rappel) == None) and (dico.get(rappel2) == None) and (dico.get(anniversaire) == None)):
        i01.speakBlocking(u"c'est l'anniversaire de personne . nous faitons "+ (saint.get(anniversaire)) )
        rest()