# -- coding: utf-8 --

security.loadStore()
keymeteo = security.getSecret("OPENWEATHERMAP")

def meteo(town,periode):
    if not runtime.isStarted('weather'):
        i01.info(u"Activation du service openweather") 
        global weather
        weather=runtime.start("weather", "OpenWeatherMap")
        weather.setKey(keymeteo) # cle api du service securite
        weather.setUnits("metric") # or imperial
        weather.setLang("fr") # fr / pour ville en france
         
     # verification de la cle api
    if keymeteo == None:
        i01.speakBlocking(u"Votre clés A P I est périmé ,ou non validé dans le service sécurity")   
    else:
        # l'unité est par pas de 3 heures (1) , de 1 à 40 ( aujourd'hui à 5 jours )
        # récupérer les données brutes pour demain (8) -> parce que 3*8=24H
        # récupérer les données brutes d'aujourd'hui (1) -> demain est 1 :
        weather.clearLastError()
        weather.setPeriod(periode)
        weather.setLocation(town+",FR")
        weather.getWeatherCode()
        error = weather.getLastError()
        if error:
            i01_chatBot.getResponse("SYSTEM openweathermapError")
        else:
            i01_chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(weather.getDegrees())) + " Town " + str(weather.getLocation().split(',')[0]) + " COMMENTAIRE " +  str(weather.getWeatherCode()) + " NBJOUR " + str(periode))
              
     
# pour mémo service météo
#print (u"Raw code : " + str(weather.getWeatherCode()))
#print (u"Ville : " + str(weather.getLocation()))
#print (u"Le temps est : "+ str(weather.getWeatherDescription()))
#print (u"Humidité : " + str(weather.getHumidity()))
#print (u"Température est :" + str(weather.getDegrees())+ u" degrés " + weather.getLocalUnits())
#print (u"Température minimun : " + str(weather.getMinDegrees()))
#print (u"Pression :" + str(weather.getPressure()))
#print (u"Vitesse du vent : " + str(weather.getWindSpeed()))
#print (u"Orientation du vent : "+str(weather.getWindOrientation()))
#i01.warn(u"met une note dans alarme.")

