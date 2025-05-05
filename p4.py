from curses.ascii import islower
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite



x1 = -100
y1 = 100
x2 = -100
y2 = 50
x3 = -100
y3 = 0
x4 = -100
y4 = -50

set_background("cornfield")
t1 = create_sprite("applecore",x1,y1)
t2 = create_sprite("bike",x2,y2)
t3 = create_sprite("flower",x3,y3)
t4 = create_sprite("fox",x4,y4)


# the bike will be the fastest because its x value increases the fastest
for i in range(30):
	x1 += 6
	x2 += 15
	x3 += 1
	x4 += random.randint(8, 20)
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)



if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("apple wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
 	print("bike wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("flower wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("fox wins!")


turtle.exitonclick()
