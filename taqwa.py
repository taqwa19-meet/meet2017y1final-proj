import turtle
import time

SIZE_X=1000
SIZE_Y=700
screen = turtle.Screen()
screen.bgpic("world_map.gif")
screen.setup(SIZE_X, SIZE_Y)
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()

ethiopia = turtle.clone()
ethiopia.shape("turtle")
ethiopia.penup()
ethiopia.goto(-50,-120)
ethiopia.pendown()
ethiopia.stamp()

ethiopia1 = turtle.clone()
ethiopia1.shape("turtle")
ethiopia1.penup()
ethiopia1.goto(-10,-130)
ethiopia1.pendown()
ethiopia1.stamp()

ethiopia2 = turtle.clone()
ethiopia2.shape("turtle")
ethiopia2.penup()
ethiopia2.goto(-20,-160)
ethiopia2.pendown()
ethiopia2.stamp()

ethiopia3 = turtle.clone()
ethiopia3.shape("turtle")
ethiopia3.penup()
ethiopia3.goto(-20,-200)
ethiopia3.pendown()
ethiopia3.stamp()

madagascar = turtle.clone()
madagascar.shape("turtle")
madagascar.penup()
madagascar.goto(50,300)
madagascar.pendown()
madagascar.stamp()

madagascar1 = turtle.clone()
madagascar1.shape("turtle")
madagascar1.penup()
madagascar1.goto(30,260)
madagascar1.pendown()
madagascar1.stamp()

madagascar2 = turtle.clone()
madagascar2.shape("turtle")
madagascar2.penup()
madagascar2.goto(10,230)
madagascar2.pendown()
madagascar2.stamp()

chad = turtle.clone()
chad.shape("turtle")
chad.penup()
chad.goto(-400,200)
chad.stamp

chad1 = turtle.clone()
chad1.shape("turtle")
chad1.penup()
chad1.goto(-430,220)
chad1.stamp

chad2 = turtle.clone()
chad2.shape("turtle")
chad2.penup()
chad2.goto(-230,180)
chad2.stamp

peru = turtle.clone()
peru.shape("turtle")
peru.penup()
peru.goto(320,40)
peru.stamp

peru1 = turtle.clone()
peru1.shape("turtle")
peru1.penup()
peru1.goto(350,60)
peru1.stamp

peru2 = turtle.clone()
peru2.shape("turtle")
peru2.penup()
peru2.goto(290,40)
peru2.stamp



afghanistan = turtle.clone()
afghanistan.shape("turtle")
afghanistan.penup()
afghanistan.goto(-300,-110)
afghanistan.stamp

afghanistan1 = turtle.clone()
afghanistan1.shape("turtle")
afghanistan1.penup()
afghanistan1.goto(-340,-90)
afghanistan1.stamp

afghanistan2 = turtle.clone()
afghanistan2.shape("turtle")
afghanistan2.penup()
afghanistan2.goto(-280,-70)
afghanistan2.stamp

pos_list = [(-50.00,-120.00), (50,300), (-400,200), (320,40), (-300,-100)]
new_pos_list = [(-10,-130)]

riddle_dict = {

        'ethiopia': {
                'question': 'A kind of tree you can carry in your hand ____',
                'answer_choices' :['dead tree' , 'palm tree' , 'apple tree' , 'lost tree'],
                'correct' : 'palm tree'
                } ,
        'ethiopia1' : {
                    'question' : "Which country's name is misspelled in our map?",
                    'answer_choices' : ['Ethiopia', 'Chad', 'Peru', 'Afghanistan'],
                    'correct' : 'Afghanistan'
                } ,
        'ethiopia2' : {
                    'question' : "What is the meaning of DU?" ,
                    'answer_choices' : ['Dear Universe', "Dr. Unicorn" , "Directly Used" , "Deeper Understanding"],
                    'correct' : "Deeper Understanding" ,
                } ,
        'ethiopia3' : {
                    'question' : "How many times does the letter A appears when counting from 1 to 100?" ,
                    'answer_choices' : ['1', '34', '0', '6'] ,
                    'correct' : '0' ,
                },
        'madagascar': {
                'question': 'What is an astronauts favourite meal?' ,
                'answer_choices' :['Launch' , 'Breakfast' , 'Dinner' , 'Brunch'],
                'correct' : 'Launch'
                } ,
        'madagascar1' : {
                'question' : 'What is the precentage of hungry people in the world?',
                'answer_choices' :['1.2', '5.7', '10.9', '21.4'],
                'correct' : '10.9'
                } ,
        'madagascar2' : {
                'question' : '2, 6, 8, 14, 22, 36, 58, ...',
                'answer_choices' : ['64', '3.1415', '94', 'all you need is math'],
                'correct' : '94'
                } ,
        'chad': {
                'question' : 'In israel there is a doctor for every 400 person , in Chad there is a doctor for every ____',
                'answer_choices' : ['47,500' , '13,750' , '23,600' , '24,600'],
                'correct' : '23,600'
                } ,
        'chad1': {
                'question' : 'How many hungry people are there in the world?',
                'answer_choices' : ['10 millions' , '795 millions' , '2.3 billions', '0'],
                'correct' : '795 millions'
                } ,
        'chad2' : {
                'question' : 'How cool is Mustafa?',
                'answer_choices' : ['High school', '10.5', 'No more than Ted', 'Air conditioner'] ,
                'correct' : 'High school'
            } ,
        'peru' : {
                'question' : 'What is orange and sounds like a parrot?',
                'answer_choices' : ['tomato' , 'orange' , 'potato' , 'carrot'],
                'correct' : 'carrot'
                } ,
        'peru1' : {
                'question' : "Who is MEET's biggest donor?",
                'answer_choices' : ['USaid', 'The Israeli government', 'Facebook', 'HP'],
                'correct' : 'USaid'
                } ,
        'peru2' : {
                'question' : "Which day is holy for Hinduism?",
                'answer_choices' : ['Tuesday', 'Saturday', 'Every Day Is Holy', 'They do not have one'],
                'correct' : 'They do not have one',
                } ,
        'afghanistan': {
                'question' : "Snake, Elephant, Tapir, ...",
                'answer_choices' : ['Rabbit' , 'Bear' , 'Ostrich' , 'Whale'],
                'correct' : 'Rabbit'
                } ,
        'afghanistan1': {
                'question' : 'How many people in the world have no access to clean water',
                'answer_choices' : ['50 millions', '100 thousands', '1 billion', '667 millions'],
                'correct' : '667 millions'
                } ,
        'afghanistan2' :{
                'question' : 'Which of the following letters appear the least in the periodic table?',
                'answer_choices' : ['Z', 'G', 'X', 'J'] ,
                'correct' : 'J'
                }
        }


turtle.register_shape('girl.gif')
turtle.shape('girl.gif')
girl = turtle.clone()
turtle.hideturtle()
girl.goto(0,0)


basket=turtle.clone()
turtle.register_shape("basket3.gif")
basket.shape("basket3.gif")
basket.penup()
basket.goto(340,300)
basket.pendown()
basket.stamp()
basket.hideturtle()
basket.penup()

score = turtle.clone()
score.goto(380, 300)
score.pendown()
cur_score = 0
score.write("score: " + str(cur_score), font=('Ariel', 11, 'normal'))
def score_counter():
    global cur_score
    cur_score+=16
    score.clear()
    score.write("score: "  + str(cur_score), font=('Ariel', 11, 'normal'))
    if cur_score == 80:
        white_stamp.showturtle()
        turtle.goto(-100, 0)
        turtle.write("You Won This Game!", font=('Ariel', 24, "normal"))
        time.sleep(2)
        quit()

mis_count = 3
mistake = turtle.clone()
mistake.goto(150, 300)
mistake.write("You have" + " " + str(mis_count) + " " + "strikes" , font=("Ariel", 11, "normal"))
def mistakes():
    global mis_count
    mis_count = mis_count - 1
    mistake.clear()
    mistake.write("You have" + " " + str(mis_count) + " " + "strikes", font=("Ariel", 12, "normal"))
    if mis_count == 0:
        white_stamp.showturtle()
        turtle.write("You Lost This Game!", font=("Ariel", 24, "normal"))
        quit()
    
turtle.shape("square")
turtle.resizemode("user")
white_stamp = turtle.clone()
white_stamp.shape("square")
white_stamp.goto(0,0)
white_stamp.color("white")
white_stamp.shapesize(100,100,0)

def answer_A():
    turtle.clear()
    turtle.goto(-230,0)
    global country
    riddle_answer = riddle_dict[country]['answer_choices'][0] == riddle_dict[country]['correct']
    if riddle_answer == True:
        turtle.write('You answered right! You prevented hunger in this country!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong! The country still suffers from food insecurity!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        mistakes()
    turtle.clear()
   
        
def answer_B():
    turtle.clear()
    turtle.goto(-230,0)
    global country
    riddle_answer = riddle_dict[country]['answer_choices'][1] == riddle_dict[country]['correct']
        
    if riddle_answer == True:
        turtle.write('You answered right! You prevented hunger in this country!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong! The country still suffers from food insecurity!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        mistakes()

    turtle.clear()
       
def answer_C():
    turtle.clear()
    turtle.goto(-230,0)
    global country
    riddle_answer = riddle_dict[country]['answer_choices'][2] == riddle_dict[country]['correct']
        
    if riddle_answer == True:
        turtle.write('You answered right! You prevented hunger in this country!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong! The country still suffers from food insecurity!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        mistakes()

    turtle.clear()
   
def answer_D():
    turtle.clear()
    turtle.goto(-230,0)
    global country
    riddle_answer = riddle_dict[country]['answer_choices'][3] == riddle_dict[country]['correct']
    
    if riddle_answer == True:
        turtle.write('You answered right! You prevented hunger in this country!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong! The country still suffers from food insecurity!', font=("Ariel", 12, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        mistakes()

    turtle.clear()
def lis():
    turtle.onkeypress(answer_A, 'a')
    turtle.onkeypress(answer_B, 'b')
    turtle.onkeypress(answer_C, 'c')
    turtle.onkeypress(answer_D, 'd')
    turtle.listen()

letters = ['a', 'b', 'c', 'd']
pos1_list= [(-SIZE_X * 0.3 - 100, SIZE_Y / 7),(-SIZE_X * 0.3 - 100, -SIZE_Y * 2 / 7),(SIZE_X * 3 / 10 - 100, SIZE_Y / 7),(SIZE_X * 3 / 10 - 100, -SIZE_Y * 2 /7)]
def riddles():
    global country, riddle_dict, letters,pos1_list
    if girl.pos() == pos_list[0]:
        country = 'ethiopia'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()

    if girl.pos() == new_pos_list[0]:
        country = 'ethiopia1'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
        
    if girl.pos() == pos_list[1]:
        white_stamp.showturtle()
        country = 'madagascar'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
                    
    if girl.pos() == pos_list[2]:
        white_stamp.showturtle()
        country='chad'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 12, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
        
    if girl.pos() == pos_list[3]:
        white_stamp.showturtle()
        country='peru'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
            
    if girl.pos() == pos_list[-1]:
        white_stamp.showturtle()
        country='afghanistan'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()


UP_EDGE = 350
DOWN_EDGE = -350
LEFT_EDGE = -500
RIGHT_EDGE = 500


def move_girl():
    my_pos = girl.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    n = 3
    if direction==UP and girl.pos()[1] <= UP_EDGE - (10 * n):
        girl.goto(x_pos, y_pos + 10)
        print("Up")
    elif direction==LEFT and girl.pos()[0] >= LEFT_EDGE + (10*n):
        girl.goto(x_pos - 10, y_pos)
        print("Left")
    elif direction==RIGHT and girl.pos()[0] <= RIGHT_EDGE - (10 * n):
        girl.goto(x_pos + 10, y_pos)
        print("Right")
    elif direction==DOWN and girl.pos()[1] >= DOWN_EDGE + (10*n):
        girl.goto(x_pos, y_pos - 10)
        print("Down")

    riddles()


turtle.penup()
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
    move_girl()
    print("you pressed the up key")

direction = DOWN
def down():
    global direction
    direction=DOWN
    move_girl()
    print("you pressed the down key")

direction = LEFT
def left():
    global direction
    direction=LEFT
    move_girl()
    print("you pressed the left key")

direction = RIGHT
def right():
    global direction
    direction=RIGHT
    move_girl()
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

dictionary = {"a kind of tree you can carry in your hand ____" : 'palm tree' , "What is an astronaut's favourite meal?____" : 'Launch' , "In israel there is a doctor fot every 400 person , in Chad there is a doctor for each ____" : '23,600' , "what's orange and sounds like a parrot?____" : 'carrot' , " Snake , Elephant , Tapir , ...": 'Rabbit' }
SIZE_X = 1000
SIZE_Y = 700



stamp = turtle.clone()
stamp.shape("square")
stamp.pensize(1000)
        

    





    
        
    
    




