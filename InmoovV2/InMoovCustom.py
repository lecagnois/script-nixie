###############################################################################
# InMoovCustom.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
# #############################################################################
# YOUR INMOOV CUSTOM SCRIPT
# Here you can add your own commands to play and test with InMoov
# This python script is located in the directory data/InMoov2/
# Those commands are safe, you can copy them to your other MRL versions
# ##############################################################################


## These samples would be executed when starting i01:

## Play a neoPixel animation while the robot speaking
#i01_neoPixel.playAnimation('Flash Random', 255, 255, 255, 1)
## Talk something
#i01_mouth.speakBlocking('he is a replicant, or not?')
## Stop neoPixel
#i01_neoPixel.stopAnimation()
## Move the index servo
#i01_rightHand_index.moveTo(20)

execfile('data/InMoov2/A_loto.py')
execfile('data/InMoov2/A_anniversaire.py')
execfile('data/InMoov2/A_bdamis.py')