#section 1: setup
import codesters
import random
from codesters import StageClass
stage = StageClass()
stage.disable_left_wall() 

stage.set_background("underwater")
player = codesters.Sprite("dolphin",-175, 0)
player.set_size(0.06)

object_speed = 5
score = 0



#section 2: objects
def falling_object():
    global object_speed,score

    if score < 5:
    #game is not over
        x = random.randint (50, 150)
        y = random.randint (-200, 200)
        object = codesters.Sprite ("beachball",x,y )
        object.set_x_speed(object_speed)
        object.set_size(0.15)

stage.event_interval (falling_object, 0.75)



#section 3: Collisions
def collision (player,object):
    global score

    if object.get_image_name() == "beachball":
        stage.remove_sprite(object)
        score+=1
        if score>=5:
                player.say(f"YOU WIN", 20)
                           
player.event_collision(collision)



#section 4: Controls
def go_up():
    player.move_up (10)
def go_down():
    player.move_down (10)

player.event_key("up", go_up)
player.event_key("down", go_down)