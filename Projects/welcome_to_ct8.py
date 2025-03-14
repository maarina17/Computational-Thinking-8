###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("chillguy",130,-175)
mySprite.set_size(1.5)
mySprite.set_opacity(0.75)
mySprite.set_rotation(10)
mySprite.say("hello coconut")






mySprite = codesters.Sprite("birdboi",-110,140)
mySprite.say("hello chill guy")
mySprite.set_rotation(-10)

mySprite = codesters.Sprite("coconut1",-175,-175)
mySprite.set_size(0.5)
mySprite.say("hello bird")