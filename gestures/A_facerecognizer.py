# Modification lecagnois  07/05/2023
def facerecognizer(): 
  #vous devez former au moins 2 FACES !
  if runtime.isStarted('i01.opencv'):
    i01_opencv.capture()
    #i01.cameraOn()
    i01_opencv.addFilter("FaceRecognizer")
    i01_opencv.setActiveFilter("FaceRecognizer")
    fr = i01_opencv.getFilter("FaceRecognizer")
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
    fr.train()# il faut un certain temps pour s entrainer et etre capable de reconnaitre le visage
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
    python.subscribe("i01.opencv", "publishRecognizedFace")
    # wait for X
    #sleep(1)
    #classifications.clear()
    #python.unsubscribe('i01.opencv', 'publishRecognizedFace')
    #01_opencv.disableFilter("FaceRecognizer")
    #i01_opencv.removeFilter('FaceRecognizer')
    #i01_opencv.stopCapture()

  else:
    errorSpokenFunc('OPENCVNOWORKY')
  i01.finishedGesture()