def playsong(data):
  #i01.startedGesture()
  if (data == "can i have your attention"): # Могу ли я привлечь ваше внимание
    i01_mouth.speak("ok you have my attention")
    #i01_mouth.speak(u"Хорошо, что я привлёк ваше внимание")
    stopit()
    i01_mouth.speak("electro funk inmoov")
    #i01_mouth.speak(u"Электо функции Инмоова")
    i01.setHeadSpeed(100.0,100.0)
    i01.setArmSpeed("left",100.0,100.0,100.0,100.0)
    i01.setArmSpeed("right",100.0,100.0,100.0,100.0)
    i01.setHandSpeed("left",100.0,100.0,100.0,100.0,100.0,100.0)
    i01.setHandSpeed("right",100.0,100.0,100.0,100.0,100.0,100.0)
    i01.setTorsoSpeed(100.0,100.0,100.0)
    #for x in range(5):
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveTorso(90,90,90)
    fullspeed()
    i01.giving()
    sleep(5)
    i01.armsFront()
    sleep(4)
    fullspeed()
    i01.daVinci()
    sleep(5)
    surrender()
    sleep(6)
    i01.giving()
    sleep(6)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    relax()
    i01.moveTorso(90,90,90)
    sleep(3)
    fullspeed()
    sleep(3)
    madeby()
    relax()
    sleep(5)
    i01.disable()
  i01.finishedGesture()

  
   

