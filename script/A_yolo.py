# -- coding: utf-8 --
last_item_found = None

# données yolo disponibles ici
def onClassification(data):
    global classifications, last_item_found
    classifications = data
    for key, value in data.items():
      print(key)
      last_item_found = key
   
def openyolo():
    global last_item_found
    if runtime.isStarted('i01.opencv'):
        i01_opencv.addFilter("yolo")
        i01_opencv.setDisplayFilter("yolo")
        i01_opencv.setCameraIndex(0)
        i01_opencv.capture()
        i01_chatBot.getResponse("YOLO_01")
        classifications = {}
        last_item_found = None
        # create a subscription to classification publication
        python.subscribe('i01.opencv', 'publishClassification')
     else:
       i01_chatBot.getResponse("YOLO_04")
   
def yolocherche() :
    global last_item_found
    if runtime.isStarted('i01.opencv') :
       #arret du scan  
       if last_item_found != None :
          python.unsubscribe('i01.opencv', 'publishClassification')
          print('dernier objet vu : ', last_item_found)
          i01_chatBot.getResponse("YOLO_02 " + last_item_found)
          last_item_found = None
       else:
          i01_chatBot.getResponse("YOLO_06")
    else:
       i01_chatBot.getResponse("YOLO_05")
       last_item_found = None
    #autre classification
    #python.unsubscribe('i01.opencv', 'publishClassification')
    #print('confiance ', classifications.get(last_item_found).get(0).getConfidence())
    #print('position ', classifications.get(last_item_found).get(0).getBoundingBox())
    
def closeyolo():
    global last_item_found
    i01_chatBot.getResponse("YOLO_03")
    last_item_found = None
    i01_opencv.removeFilter('yolo')
    i01_opencv.stopCapture()
    i01.cameraOff() 
    #runtime.release('i01.opencv')
    


    
