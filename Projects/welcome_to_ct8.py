###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("cardinal")
mySprite.say("Hello Caroline")
mySprite2 = codesters.Sprite("frank",150,-150)
mySprite2.set_size(0.5)
mySprite3 = codesters.Sprite("caroline",-150,150)
mySprite3.set_size(0.5)