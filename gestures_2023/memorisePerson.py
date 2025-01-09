from org.myrobotlab.opencv import OpenCVFilterFaceRecognizer

def YesName(name):
  print(name)
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    if runtime.isStarted('i01.opencv'):
      i01_opencv.capture()
      i01_opencv.addFilter("FaceRecognizer")
      i01_opencv.setActiveFilter("FaceRecognizer")
      # definir le nom sur le filtre qui sera utilise pour les exemples enregistres
      fr = i01_opencv.getFilter("FaceRecognizer")
      fr.setTrainName(unicode(name,'utf-8'))
      #fr.setTrainName(name)
      # set the filter to be in training mode (Where it learns new images)
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      # maintenant que nous avons de nouveaux exemples, reentrainons la reconnaissance faciale avec les exemples.
      sleep(5)
      fr.train()
      # apres que nous ayons recycle le modele .. recommencez a reconnaitre
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      i01_opencv.disableFilter("FaceRecognizer")
      i01_opencv.removeFilter("FaceRecognizer")
      #i01_opencv.stopCapture()
      i01.finishedGesture()
    else:
      i01.warn('facerecognizer ne démarre pas car opencv arreté')

def memorisePerson(name):
  if faceRecognizerActivated==1:
    print(name)
    if runtime.isStarted('i01.neoPixel'):
      i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
    if runtime.isStarted('i01.chatBot'):
      if runtime.isStarted('i01.opencv'):
        global i01_opencv
        i01_opencv = runtime.start("i01.opencv","OpenCV")
        i01_opencv.capture()
        i01_opencv.addFilter("FaceRecognizer")
        i01_opencv.setActiveFilter("FaceRecognizer")
        #  definir le nom sur le filtre qui sera utilise pour les exemples enregistres
        fr = i01_opencv.getFilter("FaceRecognizer")
        fr.setTrainName(unicode(name,'utf-8'))
        #fr.setTrainName(name)
        # set the filter to be in training mode (Where it learns new images)
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
        # maintenant que nous avons de nouveaux exemples, reentrainons la reconnaissance faciale avec les exemples.
        fr.train()
        # apres que nous ayons recycle le modele .. recommencez a reconnaitre
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
        i01_opencv.disableFilter("FaceRecognizer")
        i01_opencv.removeFilter("FaceRecognizer")
        i01_opencv.stopCapture()
        i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
        i01.finishedGesture()
      else:
        i01.warn('facerecognizer ne démarre pas car opencv arreté')
        if runtime.isStarted('i01.chatBot'):
          i01_chatBot.getResponse("NOTFACERECOGNIZED")
  else:
        i01.warn('facerecognizer is OFF')
        if runtime.isStarted('i01.chatBot'):
          i01_chatBot.getResponse("NOTFACERECOGNIZED")     
