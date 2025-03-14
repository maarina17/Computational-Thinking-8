###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("flowers")
mySprite = codesters.Sprite("penguin",0,-50)
mySprite.set_size(0.5)
mySprite.say("Hi Emily!!!!")


mySprite2 = codesters.Sprite("baseball",-150,150)

print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last instruction")