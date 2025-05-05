import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Interactive Drawing")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(20)

def rotate_angle_left():
    turtle_instance.left(20)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun= turtle_forward, key= "space")
drawing_board.onkey(fun= rotate_angle_right, key= "Right")
drawing_board.onkey(fun= rotate_angle_left, key= "Left")
drawing_board.onkey(fun= clear_screen, key= "c")
drawing_board.onkey(fun= turtle_return_home, key= "h")
drawing_board.onkey(fun= turtle_pen_up, key= "u")
drawing_board.onkey(fun= turtle_pen_down, key= "d")


turtle.mainloop()