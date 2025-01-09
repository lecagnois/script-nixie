# -- coding: utf-8 --
def imagephoto() :

	# si open cv deja lancer
	if runtime.isStarted('opencv') and runtime.isStarted('i01.mouth.audioFile'):
		i01.speakBlocking(u"regarde moi bien dans les yeux , le petit oiseau va sortir")
		#ajouter le fichier click.mp3 dans ../data/sounds
		AudioPlayer.playFile('data/sounds/click.mp3')
		#sauve image dans data /opencv
		cv.saveImage() 
   
	else:  
		# creation du service open cv , i01.mouth et parametrage 
		i01 = runtime.start('i01','InMoov2')
		AudioPlayer = runtime.start('i01.mouth.audioFile', 'AudioFile')
		cv = i01.startPeer('opencv')
		cv.addFilter("pdown","PyramidDown")
		cv.setDisplayFilter("pdown")
		cv.setCameraIndex(0)
		cv.capture()
		i01.speakBlocking("regarde moi bien dans les yeux , le petit oiseau va sortir")
		#ajouter le fichier click.mp3 dans ../data/sound
		AudioPlayer.playFile('data/sounds/click.mp3')
		#sauve image dans data /opencv
		cv.saveImage() 
  
	sleep(5)
	cv.removeFilter('pdown') # supprime le filtre
	cv.stopCapture() # arrete capture
	i01.speakBlocking(u"j'ai enregistré la photo dans ma memoire")
	#i01.cameraOn()  allume lacamera
	#i01.cameraOff()  eteint lacamera
