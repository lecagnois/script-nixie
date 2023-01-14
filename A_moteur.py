# -- coding: utf-8 --
#########################################
# MotorDualPwm.py
# moteur pour plateforme inmoov
# categories: motor
# more info @: http://myrobotlab.org/service/MotorDualPwm
#########################################
# port com de l arduino du plateau motorise
port="COM6"
#declaration  2 moteurs 
arduino = Runtime.start("arduino","Arduino")
motor1 = Runtime.start("motor1","MotorDualPwm")
motor2 = Runtime.start("motor2","MotorDualPwm")
sr04 = Runtime.start("sr04", "UltrasonicSensor")
arduino.connect(port)
# initialisation des broches arduino
motor1.setPwmPins(10,11)
motor2.setPwmPins(5,6)
motor1.attach(arduino)
motor2.attach(arduino)
sr04.attach(arduino, 4, 3)
#ecouteur du capteur ultrason
sr04.addRangeListener(python)

def onRange(distance):
    #print distance, " cm"
    # si inferieur a 20 cm arrete les moteurs
    if (distance <=20) :
        motor1.stop()
        motor2.stop()
        sr04.stopRanging()
        myRange = sr04.range()
        print ("obstacle a " + str(distance) + " cm")
        #i01.speakBlocking("oups un obstacle a " + str(distance) + u"centimètre")
        
def avance() :
    motor1.move(1)
    motor2.move(1)
    #demarre ultrason
    sr04.startRanging()
            
def recule() :
    motor1.move(-1)
    motor2.move(-1)
   
def stop() :
    #arrete les moteurs 
    motor1.stop()
    motor2.stop()	
    detachemoteur()
    #arrete ultrason
    sr04.stopRanging()
        
def tourneD() :
    motor1.move(-1)
    motor2.move(1)
    sr04.startRanging()
      
def tourneG() :
    motor1.move(1)
    motor2.move(-1)
    sr04.startRanging()
   
def detachemoteur() :
    motor1.detach(arduino)
    motor1.detach(arduino)