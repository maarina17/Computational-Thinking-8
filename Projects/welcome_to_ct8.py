###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("capybara")
mySprite.say("hi!")

mySprite2 = codesters.Sprite("malaya_sarani",-150,100)


mySprite3 = codesters.Sprite("flowers",-80,-80)