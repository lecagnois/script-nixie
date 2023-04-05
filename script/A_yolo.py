## Filtre Yolo 
# Nous classons les objets par image et obtenons le maximum detecte pour 1 image seulement
# Ainsi nous pouvons lister et compter en meme temps chaque objet classifie disponible dans le champ de vision, dans un temps donne
# Obtient egalement la position de l element donne (last_item_found) si defini de tous les autres dans le champ hors vue de gauche a droite
# classifications est le dictionnaire des objets detectes dans un temps donne
# apres acquisition et le tri des positions nous lirons le contenu de la collection pour jouer avec
## avertissement l editeur yolo est maintenant a l interieur de java land pour eviter les problemes de thread a cause du sommeil de python
# Modification lecagnois  05/04/2023
global classifications, last_item_found

def onClassification(data):
    global last_item_found
    last_item_found = None
    global classifications, last_item_found
    classifications = data
    for key, value in data.items():
        #print(key)
        last_item_found = key

def startYoloInventory(duration):
  global classifications, last_item_found
  i01.speakBlocking(i01_chatBot.getPredicate("startupSentence"))
  #if runtime.isStarted('i01.neoPixel'):
    #i01_neoPixel.setAnimation("Color Wipe", 25, 5, 10, 15)
  #Lance function to start & stop yolo filter
  enableYoloFor(duration)
  # cherche la valeur dans la class
  collectionString=""
  for key, value in classifications.items():
    collectionString=collectionString+" "+key+", "
  i01_chatBot.setPredicate("yoloTotalDetected",str(len(classifications)))
  return collectionString

def getYoloPosition(objet):
  global classifications, last_item_found
  i01.speakBlocking(i01_chatBot.getPredicate("startupSentence"))
  #Lance function to start & stop yolo filter
  enableYoloFor(6)
  # cherche la valeur dans la class
  collectionString=""
  for key, value in classifications.items():
    collectionString=collectionString+key+" "
  #print(unicode(objet, "utf-8"))
  #print(collectionString) 
  # position de l objet yolo sauve dans predicate
  i01_chatBot.setPredicate("yoloTotalDetected",str(len(classifications)))
  # unicode pour les accents et lower pour la majuscules
  if (unicode(objet, "utf-8")) in (collectionString.lower()) :
    i01.speak("j'ai trouver "+(i01_chatBot.getPredicate("article"))+" "+ unicode(objet, "utf-8") + "en position " + str(i01_chatBot.getPredicate("yoloTotalDetected")))
  else:
    i01.speak("Je ne vois pas" + (i01_chatBot.getPredicate("article"))+" "+ unicode(objet, "utf-8"))

# function to start & stop yolo filter et tempo classification
def enableYoloFor(duration):
  global lastPhotoFileName
  #start i01.opencv avec filtre yolo
  if runtime.isStarted('i01.opencv'):
    i01_opencv.addFilter("yolo")
    i01_opencv.setDisplayFilter("yolo")
    i01_opencv.setCameraIndex(0)
    i01_opencv.capture()
    classifications = {}
    # create a subscription to classification publication
    python.subscribe('i01.opencv', 'publishClassification')
    # wait for X
    sleep(duration)
    lastPhotoFileName = i01_opencv.recordFrame()
    classifications.clear()
    python.unsubscribe('i01.opencv', 'publishClassification')
    i01_opencv.disableFilter("yolo")
    i01_opencv.removeFilter('yolo')
    i01_opencv.stopCapture()
    i01.cameraOff()
