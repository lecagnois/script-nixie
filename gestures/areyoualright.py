def areyoualright():
  #i01.startedGesture()
  i01.setHeadSpeed(43.0,100.0,43.0,43.0,100.0)
  i01.moveHead(90,60,90,180,65)
  sleep(0.5)
  i01.moveHead(90,120,90,180,65)
  sleep(0.7)
  i01.moveHead(90,60,90,180,65)
  sleep(0.7)
  i01.moveHead(90,120,90,180,65)
  sleep(0.7)
  i01.moveHead(90,90,90,180,65)
  sleep(0.7)
  x = (random.randint(1, 2))
  if x == 1:
    i01_mouth.speak("i am very, super, mega bored")
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0)
    i01.moveHead(90,90,90,90,65)
    sleep(1)
    relax()
  if x == 2:
    i01_mouth.speak("I feel like a machine, doing the same thing over and over")
    i01.moveArm("left",85,93,42,16)
    i01.moveArm("right",87,93,37,18)
    i01.moveHand("left",124,82,65,81,41,143)
    i01.moveHand("right",59,53,89,61,36,21)
    i01.moveTorso(90,90,90)
    sleep(0.2)
    i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0)
    i01.moveHead(90,90,90,90,65)
    sleep(1)
  i01.finishedGesture()
  relax()