# Modification lecagnois  22/06/2023
def facerecognizer(): 
  #you need to train at least 2 FACES !
  if not runtime.isStarted('i01.opencv'):
    errorSpokenFunc('OPENCVNOWORKY')
    i01.info(u"Activation du service OpenCv") 
    opencv = runtime.start('i01.opencv', 'OpenCV')
  else:
    i01.speakBlocking(u"Je démarre le module d'analyse des visages.")
    i01_opencv.capture()
    i01_opencv.addFilter("FaceRecognizer")
    i01_opencv.setActiveFilter("FaceRecognizer")
    fr = i01_opencv.getFilter("FaceRecognizer")
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
    fr.train()# it takes some time to train and be able to recognize face
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
    python.subscribe("i01.opencv", "publishRecognizedFace")

  i01.finishedGesture()
