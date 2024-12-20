# -- coding: utf-8 --
# ##############################################################################
# 								TIMERS ACTION
# Timer reveil matin
#lecagnois le 21/12/2024
###############################################################################
import time
from datetime import datetime

def reveilstart(tmpreveil):
    global hreveil
    global mreveil
    # mise en forme heure 
    # cas 18 heures pile
    if len(tmpreveil) == 3 :
        hreveil = str(tmpreveil[0:-1])
        mreveil =  "00"
    # cas 1h30 du matin
    if len(tmpreveil) == 4 :
        hreveil = ("0"+str(tmpreveil[0:-3]))
        mreveil =  str(tmpreveil[2:4])
    if len(tmpreveil) == 5 :
        hreveil = str(tmpreveil[0:-3])
        mreveil =  str(tmpreveil[3:5])
    if (len(tmpreveil) > 5) or (tmpreveil=="midi") : 
        i01_chatBot.getResponse("REVEIL_01")
        return
    #print(hreveil)
    #print(mreveil)
    # lancement du timer
    ReveilTime = Runtime.start("ReveilTime","Clock")
    ReveilTime.setInterval(60000)
    #lance la fonction toutes les minutes
    ReveilTime.addListener("pulse", python.name, "ReveilTime_def")
    ReveilTime.startClock()
    i01.speak(u"réveil activé") 

def reveilstop():
    #arret du timer reveil
    ReveilTime.stopClock()
    i01.speak(u"reveil désactivé") 
    ReveilTime.stopService()
    runtime.release('ReveilTime')

def ReveilTime_def(timedata):
    global hreveil
    global mreveil
    minute = str(timedata)[14:16]
    heure = str(timedata)[11:13]
    print ("temps machine : "+heure +" " + minute)
    print( "heure Reveil : " + hreveil +" " + mreveil)
    # donne l heure avec humour 
    if heure == hreveil and minute == mreveil :
        #print(u"c'est l'heure")
        # lance la musique au hasard
        playRandomMusic()


