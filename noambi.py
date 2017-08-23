import turtle
SIZE_X=1000
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()

turtle.goto(-400,50)
turtle.pendown()
turtle.goto(340,50)
turtle.penup()
turtle.goto(-350,50)
turtle.pendown()
turtle.goto(-350,230)



ethiopia = turtle.clone()
ethiopia.shape("square")
ethiopia.penup()
ethiopia.goto(-350,250)
ethiopia.pendown()
ethiopia.stamp()



madagascar = turtle.clone()
madagascar.shape("circle")
madagascar.penup()
madagascar.goto(-300,-150)
madagascar.pendown()
madagascar.stamp()



chad = turtle.clone()
chad.shape("arrow")
chad.penup()
chad.goto(280,-200)
chad.stamp


peru = turtle.clone()
peru.shape("turtle")
peru.penup()
peru.goto(200,280)
peru.stamp

afghnistan= turtle.clone()
afghnistan.shape("classic")
afghnistan.penup()
afghnistan.goto(360,50)
afghnistan.stamp

