###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("flowers")
q1 = codesters.Square(100, 100, 200, 'white')
q2 = codesters.Square(-100, 100, 200, 'firebrick')
q3 = codesters.Square(-100, -100, 200, 'PowderBlue')
q4 = codesters.Square(100, -100, 200, 'plum')

s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite("dog", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite("controller", 100, -100)
s3.set_size(0.15)
s4 = codesters.Sprite("theatre-removebg-preview", -100, 100)
s4.set_size(0.5)

message1=codesters.Text ("Marina Harper Herrmann",0,220,"black")
message2=codesters.Text ("Better Late Than Never",0,-220,"black")