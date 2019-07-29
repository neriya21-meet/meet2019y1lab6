import turtle
turtle.goto(0,0)

turtle.color('purple')
turtle.pensize(6)
turtle.bgcolor('silver')
turtle.direction = None
    
def up():   
    turtle.direction = 'Up'
    on_move()
    print("up! yee went up!")

turtle.onkeypress(up, 'Up')

def down():
    turtle.direction = 'Down'
    on_move()
    print('yeehooo! down!')

turtle.onkeypress(down, 'Down')

def right():
    turtle.direction = 'Right'
    on_move()
    print(' aright we go!')

turtle.onkeypress(right, 'Right')

def left():
    turtle.direction = 'Left'
    on_move()
    print(' lefty! lefty!')

turtle.onkeypress(left, 'Left')
    
turtle.listen()

def on_move():
    my_pos = turtle.pos()
    X_pos =my_pos[0]
    Y_pos = my_pos[1]
    
    if turtle.direction == 'Up':
        turtle.goto(X_pos,Y_pos+50)
    elif turtle.direction == 'Down':
        turtle.goto(X_pos,Y_pos-50)
    elif turtle.direction == 'Left':
        turtle.goto(X_pos - 50, Y_pos)
    elif turtle.direction == 'Right':
        turtle.goto(X_pos + 50, Y_pos)
        





##def down():
##    turtle.back(50)
##def left():
##    turtle.left(50)
##def right():
##    turtle.right(50)

    
##turtle.onkeypress(up, "w")
##
##turtle.onkeypress(down, "s")
##
##turtle.onkeypress(left, "a")    
##
##turtle.onkeypress(right, "d")
##
##turtle.listen()

turtle.mainloop()



