# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite("waterbottle")
s2 = create_sprite("fox")
s3 = create_sprite("soccerball")
s4 = create_sprite("pinetree")
s5 = create_sprite("applecore")
s1.goto(-250, -75)
s3.goto(250,75)
s4.goto(-300, 200)
s5.goto(300, 225)

set_background("cornfield")
# TODO - set the starting value for your variable


def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)
# TODO - pick keys for each control

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Section 4: Game Loop
window.listen()

while True:
	if get_distance(s1, s2) < 100:
		break
	if get_distance(s1, s3) < 100:
		break
	if get_distance(s1, s4) < 175:
		print("Game Over")
		break
	if get_distance(s1, s5) <50:
		print("Winner")
		break
		

	 
    
 	# TODO - code for automatic actions






	window.update()

	# if :
	# 	break
	


