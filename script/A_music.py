# -- coding: utf-8 --
import os

def chercheplay(morceau):
    if runtime.isStarted('i01.audioPlayer'):
        if os.path.exists('data/config/default/i01.audioPlayer.yml'):
                global liste
                global pointeur
                i01.speakBlocking(u"oké voici le morceau")
                f = open('data/config/default/i01.audioPlayer.yml', 'r')
                liste = f.readlines()
                #supprime les 11 premiers elements de la liste
                del liste[0:11]
                i=0
                flag =0
                # iteration sur la liste avec mise en forme de la chaine
                while i <= len(liste)-2 :  
                    var = unicode("".join(liste[i][4:]).rstrip('\n'),'utf-8')
                    #if " "+morceau+" " in (" " + var + " "):
                    if (morceau.lower() in var) or (morceau.capitalize() in var):
                        i01_audioPlayer.play(var)
                        pointeur = i
                        flag = 1
                        print(var+" Morceau : "+str(pointeur))
                    i=i+1
                if flag == 0 :
                    i01.speakBlocking(u"Je n'ai pas ce morceau dans mes listes. ou le fichier contient des majuscules.")
                f.close()
        else:
            i01.speakBlocking(u"Je n'ai pas de playlist configuré dans le répertoire default")
    else :
        i01.speakBlocking(u"Le service audio player n'es pas lancé. Je le démarre.") 
        AudioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')
        
def nextplay():
    if runtime.isStarted('i01.audioPlayer'):
        global pointeur 
        pointeur = pointeur + 1
        i01_audioPlayer.stop()
        var = unicode("".join(liste[pointeur][4:]).rstrip('\n'),'utf-8')
        if 'mp3' in var :
            i01_audioPlayer.play(var)
            print(var+" Morceau : "+str(pointeur))
        else:
            i01.speakBlocking(u"Je suis arrivé à la fin de la play liste. Je remonte au début de la liste")
            pointeur = -1
            i01_audioPlayer.stop()
            i01_chatBot.getResponse("SYSTEM MORCEAU SUIVANT")
    else :
        i01.speakBlocking(u"Le service audio player n'es pas lancé. Je le démarre.") 
        AudioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')
   
def previousplay():
    if runtime.isStarted('i01.audioPlayer'):
        global pointeur 
        pointeur = pointeur -1
        i01_audioPlayer.stop()
        var = unicode("".join(liste[pointeur][4:]).rstrip('\n'),'utf-8')
        if 'mp3' in var :
            i01_audioPlayer.play(var)
            print(var+" Morceau : "+str(pointeur))
        else:
            i01.speakBlocking(u"Je suis arrivé au début de la play liste. Je remonte au début de la liste")
            pointeur = -1
            i01_audioPlayer.stop()
            i01_chatBot.getResponse("SYSTEM MORCEAU SUIVANT")
    else :
        i01.speakBlocking(u"Le service audio player n'es pas lancé. Je le démarre.") 
        AudioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')   
        
def playRandomMusic():
    if runtime.isStarted('i01.audioPlayer'):
        if os.path.exists('data/config/default/i01.audioPlayer.yml'):
            audioConfig = i01_audioPlayer.getConfig().currentPlaylist
            i01_audioPlayer.startPlaylist(audioConfig,1,0)
           # (Nom de playlist,Nb de fois aléatoire, boolean repeat, String track)
        else:
            i01.warn(u"Je n'ai pas de playlist configuré dans le répertoire default")
    else:
        i01.speakBlocking(u"Le service audio player n'es pas lancé. Je le démarre.") 
        AudioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')    