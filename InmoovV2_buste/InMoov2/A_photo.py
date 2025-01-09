# -- coding: utf-8 --
def imagephoto(image) :
	# si open cv deja lancer
	if runtime.isStarted('i01.opencv') and runtime.isStarted('i01.mouth.audioFile'):
		if image =="droite":
			i01.setHeadSpeed(22.0, 22.0)
			i01.moveHead(180,90)
			i01.finishedGesture()
		if image =="gauche":
			i01.setHeadSpeed(22.0, 22.0)
			i01.moveHead(90,180)
			i01.finishedGesture()	
		if image =="centre":
			i01.setHeadSpeed(22.0, 22.0)
			i01.moveHead(90,100)
			i01.finishedGesture()

		audioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')
		i01.speakBlocking(u"regarde moi bien dans les yeux , le petit oiseau va sortir")
		audioPlayer.playFile('data/sounds/click.mp3')
		cv = i01.startPeer('opencv')
		cv.addFilter("pdown","PyramidDown")
		cv.setDisplayFilter("pdown")
		cv.setCameraIndex(0)
		cv.setGrabberType("VideoInput")
		cv.capture()
		sleep(2)
		cv.saveImage()
		cv.removeFilter('pdown') # supprime le filtre
		cv.stopCapture() # arrete capture
		i01.speakBlocking(u"j'ai enregistré la photo dans ma memoire")
        
	else:  
		i01.speakBlocking(u"Je ne voie rien, vérifie mes yeux.")

