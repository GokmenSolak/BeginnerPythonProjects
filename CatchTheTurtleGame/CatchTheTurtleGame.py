import turtle
import random
import time


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial", 18, "normal")
score = 0
game_is_on = True

score_turtle = turtle.Turtle()
count_down_turtle = turtle.Turtle()

def setup_scoreboard():
    score_turtle.color("Dark Blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(x=0, y=270)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

t = turtle.Turtle()
def make_turtle():
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.shape("turtle")
    t.color("Green")
    t.shapesize(stretch_wid=1.5, stretch_len=1.5)
    t.penup()
    t.hideturtle()
    t.goto(random.randint(-270, 270), random.randint(-270, 270))
    t.showturtle()
    time.sleep(0.5)

def countdown(time):
    count_down_turtle.hideturtle()
    count_down_turtle.color("Red")
    count_down_turtle.penup()
    count_down_turtle.goto(x=0, y=240)
    count_down_turtle.clear()
    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)
    else :
        global game_is_on
        game_is_on = False
        count_down_turtle.clear()
        count_down_turtle.write(arg="Game Over", move=False, align="center", font=FONT)

def start_game():
    turtle.tracer(0)
    setup_scoreboard()
    countdown(30)
    turtle.tracer(1)

    t.hideturtle()
    time.sleep(2)
    while game_is_on:
        make_turtle()
    t.hideturtle()

start_game()

turtle.mainloop()
