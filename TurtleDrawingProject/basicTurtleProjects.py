import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

#square
'''
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
    turtle.done()
'''

#star
'''
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.forward(300)
    turtle_instance.right(144)
turtle.done()
'''

#polygon
'''
turtle_instance = turtle.Turtle()
number_sides = 8
angle_of_side = 360 / number_sides
side_length = 100

for i in range(number_sides):
    turtle_instance.forward(side_length)
    turtle_instance.right(angle_of_side)
turtle.done()
'''