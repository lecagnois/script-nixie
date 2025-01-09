# -- coding: utf-8 --
# ##############################################################################
# 								TIMERS ACTION
# Timer donne l heure toutes les heures maj le 20/12/2024
# plus phrase aleatoire toutes les 15 minutes
###############################################################################

def humeurstart():
	#AudioPlayer = runtime.start('AudioPlayer', 'AudioFile')
	#AudioPlayer = runtime.getService("i01.mouth.audiofile")
    if runtime.isStarted('HumerTime'):
        i01.speak(u"Les humeurs sont déjà activées")
    else:
        HumerTime = Runtime.start("HumerTime","Clock")
        HumerTime.setInterval(60000)
        #lance la fonction toutes les minutes
        HumerTime.addListener("pulse", python.name, "HumerTime_def")
        HumerTime.startClock()
        i01.speak(u"humeur activé") 
	
def humeurstop():
    HumerTime.stopClock()
    i01.speak(u"humeur désactivé") 
    HumerTime.stopService()
    runtime.release('HumerTime')

def HumerTime_def(timedata):
    AudioPlayer = runtime.start('i01.mouth.audioFile', 'AudioFile')
    minute = str(timedata)[14:16]
    heure = str(timedata)[11:13]
    # donne l heure avec humour 
    if minute =="00" :
        Mheure = (str(random.randint(1,5))+".mp3")
        AudioPlayer.playFile('data/sounds/heure/'+heure+'/'+Mheure)
    #lance une humeur au hasard 10 minutes
    #if minute=="08" or minute=="16" or minute=="24" or minute=="37" or minute=="41"or minute=="51":
    #lance une humeur au hasard 15 minutes
    if  minute=="15" or minute=="30" or minute=="45":
        surprise = (str(random.randint(1,305))+".mp3")
        AudioPlayer.playFile('data/sounds/surprise/'+surprise)
       
# routine pour activer les oreilles depuis android
def oreillesON():
    if runtime.isStarted('watchMicro'):
        i01.speak(u"Les oreilles sont déjà activées")
    else:  
        watchMicro = runtime.start("watchMicro","Clock")
        watchMicro.setInterval(60000) 
        watchMicro.addClockEvent("python","exec", "restartListening()")
        watchMicro.startClock()
        i01_ear = runtime.start("i01.ear","WebkitSpeechRecognition")
        subprocess.call(["data/F5.exe"])
        i01_ear.startListening()
    
def oreillesOFF():
    if runtime.isStarted('watchMicro'):
        watchMicro.stopClock()
        watchMicro.stopService()
        runtime.release('watchMicro')
        runtime.release("i01.ear")
        i01.invoke("publishEvent", "STOPPED EAR")
    else:
        i01.speak(u"Les oreilles sont déjà désactivées")
        
# routine pour activer LLM depuis android    
def iaOFF():
    if runtime.isStarted('i01.llm'):
        runtime.release("i01.llm")
        i01.invoke("publishEvent", "STOPPED LLM")
    else:
        i01.speak(u"Mon Intéligence artificielle est déjà désactivé")

def iaON():
    if runtime.isStarted('i01.llm'):
        i01.speak(u"Mon Intéligence artificielle est déjà activé")
    else:  
        initLlm()
        runtime.start("i01.llm","LLM")
