import turtle
import time
import random

win = turtle.Screen()
win.title("snake")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.dir = "stop"
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)

body = []
pts = 0
best = 0

# text drawer
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")
writer.goto(0, 255)
writer.write("Score: 0 | High: 0", align="center", font=("Arial", 16, "bold"))


def up():
    if head.dir != "down":
        head.dir = "up"

def down():
    if head.dir != "up":
        head.dir = "down"

def left():
    if head.dir != "right":
        head.dir = "left"

def right():
    if head.dir != "left":
        head.dir = "right"

win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")


def reset_game():
    global pts
    time.sleep(0.8)
    head.goto(0, 0)
    head.dir = "stop"
    for part in body:
        part.goto(1000, 1000)
    body.clear()
    pts = 0
    writer.clear()
    writer.write(f"Score: {pts} | High: {best}", align="center", font=("Arial", 16, "bold"))


while True:
    win.update()

    # wall hit
    if abs(head.xcor()) > 285 or abs(head.ycor()) > 285:
        reset_game()

    # food collision
    if head.distance(apple) < 20:
        apple.goto(random.randint(-260, 260), random.randint(-260, 260))

        tail = turtle.Turtle()
        tail.shape("square")
        tail.color("lime")
        tail.penup()
        body.append(tail)

        pts += 10
        if pts > best:
            best = pts
        writer.clear()
        writer.write(f"Score: {pts} | High: {best}", align="center", font=("Arial", 16, "bold"))

    for idx in range(len(body) - 1, 0, -1):
        body[idx].goto(body[idx - 1].xcor(), body[idx - 1].ycor())

    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    if head.dir == "up":
        head.sety(head.ycor() + 20)
    elif head.dir == "down":
        head.sety(head.ycor() - 20)
    elif head.dir == "left":
        head.setx(head.xcor() - 20)
    elif head.dir == "right":
        head.setx(head.xcor() + 20)

    for part in body:
        if part.distance(head) < 15:
            reset_game()
            break

    time.sleep(0.09)