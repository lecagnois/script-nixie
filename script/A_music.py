# -- coding: utf-8 --
import os


def chercheplay(morceau):
    if runtime.isStarted('i01.audioPlayer'):
        if os.path.exists('data/config/default/i01.audioPlayer.yml'):
            i01.speakBlocking(u"fichier de configuration présent")
            f = open('data/config/default/i01.audioPlayer.yml', 'r')
            liste = f.readlines()
            #supprime les 11 premiers elements de la liste
            del liste[0:11]
            i=0
            flag =0
            # iteration sur la liste avec mise en forme de la chaine
            while i <= len(liste)-2 :  
                var = "".join(liste[i][4:]).rstrip('\n')
                #if " "+morceau+" " in (" " + var + " "):
                if morceau.lower() in var :
                    i01_audioPlayer.play(var)
                    flag = 1
                    print(var)
                i=i+1
            if flag == 0 :
                i01.speakBlocking(u"Je n'ai pas ce morceau dans mes listes. ou le fichier contient des majuscules.")
            f.close()
        else:
            i01.speakBlocking(u"Je n'ai pas de playlist configuré dans le répertoire default")
            print("ko")
    else:
        i01.speakBlocking(u"Le service player n'es pas lancé.")
