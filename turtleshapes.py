import  turtle 


num_pts = 3

for i in range (num_pts):
    turtle. left(360/num_pts)
    turtle.forward(100)

turtle.penup()
turtle.goto(200,100)
turtle.pendown()

num_pts = 7

for d in range (num_pts):
    turtle.right(360/num_pts)
    turtle.forward(50)

turtle.penup()
turtle.goto(300,100)
turtle.pendown()

turtle.goto(300,200)
for d in range (num_pts):
    turtle.right(360/num_pts)
    turtle.forward(30)

