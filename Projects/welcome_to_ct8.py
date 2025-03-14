###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("wherethefishare")
mySprite = codesters.Sprite("spinnerfish",100,50)
mySprite.say("hello guys")
mySprite.set_size(0.75)


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
mySprite2 = codesters.Sprite("turtleneck",-100,100)
mySprite2.say("hello")
mySprite2.set_size(0.75)

mySprite3 = codesters.Sprite("goofyfish",100,-150)
mySprite3.say("how you doing?")
mySprite3.set_size(0.75)