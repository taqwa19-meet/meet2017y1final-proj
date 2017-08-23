import turtle
##stamp = turtle.clone()
##stamp.shape("square")
##stamp.pensize(1000)
##dictionary = {"a kind of tree you can carry in your hand ____" : 'palm tree' , "What is an astronaut's favourite meal?____" : 'Launch' , "In israel there is a doctor fot every 400 person , in Chad there is a doctor for each ____" : '23,600' , "what's orange and sounds like a parrot?____" : 'carrot' , " Snake , Elephant , Tapir , ...": 'Rabbit' }
##SIZE_X = 1000
##SIZE_Y = 700
##riddle_dict = {
##
##        'ethiopia': {
##                'question': 'a kind of tree you can carry in your hand____',
##                'answers_choices' :['dead tree' , 'palm tree' , 'apple tree' , 'lost tree'],
##                'correct' : 'palm tree'
##                }
##        'madagascar': {
##                'question': 'What is an astronauts favourite meal?____' ,
##                'answer_choices' :['Launch' , 'Breakfast' , 'Dinner' , 'Brunch'],
##                'correct' : 'Launch'
##                }
##        'chad': {
##                'question' : 'In israel there is a doctor for each 400 person , in Chad there is a doctor foe each ____',
##                'answer_choices' :['47,500' , '13,750' , '23,600' , '24,600'],
##                'correct' : '23,600'
##                }
##        'peru': {
##                'question': 'what is orange and sounds like a parrot?____',
##                'answer_choices' :['tomato' , 'orange' , 'potato' , 'carrot'],
##                'correct' : 'carrot'
##                }
##        'afghaniatan': {
##                'question' : 'Snake' , 'Elephant' , 'Tapir' , '...',
##                'answer_choices' :['Rabbit' , 'Bear' , 'Ostrich' , 'Whale'],
##                'correct' : 'Rabbit'
##                }
##        }
##  
##def answer_A():
##        turtle.clear()
##        turtle.goto(0,0)
##        turtle.write('You answered right')
##        
##def answer_B():
##        turtle.clear()
##        turtle.goto(0,0)
##        turtle.write('You answered wrong')
##        
##def answer_C():
##        turtle.clear()
##        turtle.goto(0,0)
##        turtle.write('You answered wrong')
##        
##def answer_D():
##        turtle.clear()
##        turtle.goto(0,0)
##        turtle.write('You answered wrong')
##        
##turtle.onkeypress(answer_A, 'a')
##turtle.onkeypress(answer_B, 'b')
##turtle.onkeypress(answer_C, 'c')
##turtle.onkeypress(answer_D, 'd')
##turtle.listen()
##def riddles():
##	if girl.pos() == ethiopia:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
##		turtle.pendown()
##		turtle.write("a kind of tree you can carry in your hand____")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("a/palm tree")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("b/lost tree")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10,SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("c/apple tree")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10,-SIZE_Y * 2 / 7 )
##		turtle.pendown()
##		turtle.write("d/dead tree")
##		
##	if girl.pos() == madagascar:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7 )
##		turtle.pendown()
##		turtle.write("What's an astronaut's favourite meal?____")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("a/Launch")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("b/Breakfast")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("c/Dinner")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10, -SIZE_Y * 2 /7)
##		turtle.pendown()
##		turtle.write("d/Brunch")
##			
##	if girl.pos() == chad:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 /7)
##		turtle.pendown()
##		turtle.write("In israel there is a doctor for every 400 person , in Chad there is a doctor for each____")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("a/23,600")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("b/24,600")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("c/13,750")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10,-SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("d/47,500")
##		
##	if girl.pos() == peru:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
##		turtle.pendown()
##		turtle.write("what's orange and sounds like a parrot?____")
##		turtle.penup()
##		turtle.goto(-SIZE_Y * 0.3, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("a/carrot")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("b/orange")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("c/tomato")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10,-SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("d/potato")
##		
##		
##	if girl.pos() == afghanistan:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
##		turtle.pendown()
##		turtle.write("Snake , Elephant , Tapir , ...")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("a/Rabbit")
##		turtle.penup()
##		turtle.goto(-SIZE_X * 0.3, -SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("b/Bear")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 /10, SIZE_Y / 7)
##		turtle.pendown()
##		turtle.write("c/Ostrich")
##		turtle.penup()
##		turtle.goto(SIZE_X * 3 / 10,-SIZE_Y * 2 / 7)
##		turtle.pendown()
##		turtle.write("d/Whale")
##		
##girl = turtle.clone()
##ethiopia = girl.pos()
##madagascar = girl.pos()
##chad = girl.pos()
##peru = girl.pos()
##afghanistan = girl.pos()
##
##
##riddles()

image = 'girl.gif'
girl = turtle.clone()
turtle.shape(image)
