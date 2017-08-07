import turtle
turtle.penup()
monkey = turtle.clone()
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direction = UP
def up():
    global direction
    direction=UP
    move_monkey()
    print("you pressed the up key")

direction = DOWN
def down():
    global direction
    direction=DOWN
    move_monkey()
    print("you pressed the down key")

direction = LEFT
def left():
    global direction
    direction=LEFT
    move_monkey()
    print("you pressed the left key")

direction = RIGHT
def right():
    global direction
    direction=RIGHT
    move_monkey()
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

def move_monkey():
    my_pos = monkey.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==UP:
        monkey.goto(x_pos, y_pos + 10)
        print("Up")
    elif direction==LEFT:
        monkey.goto(x_pos - 10, y_pos)
        print("Left")
    elif direction==RIGHT:
        monkey.goto(x_pos + 10, y_pos)
        print("Right")
    elif direction==DOWN:
        monkey.goto(x_pos, y_pos - 10)
        print("Down")
        
