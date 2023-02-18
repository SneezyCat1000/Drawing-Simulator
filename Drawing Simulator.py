#Window
import turtle
import time
win = turtle.Screen()
win.title("Drawing Simulator")
win.bgcolor("black")

#instructions
print("arrow keys to move")
print("colors:")
print("r = red, o = orange, y = yellow, g = green, b = blue, v = violet, p = pink")
print("background:")
print("1 = white, 2 = black")
print("disable ink = space, enable ink = z")

#Triangle Set
Tri = turtle.Turtle()
Tri.shape("triangle")
Tri.color("gold")
Tri.shapesize(stretch_wid=1, stretch_len=1)
Tri.speed(0)
Tri.setheading(90)

#Move Definitions
def bg_black():
    win.bgcolor("Black")

def bg_white():
    win.bgcolor("White")

def Tri_up():
    y = Tri.ycor()
    y += 10
    Tri.sety(y)
    Tri.setheading(90)

def Tri_down():
    y = Tri.ycor()
    y -= 10
    Tri.sety(y)
    Tri.setheading(-90)

def Tri_right():
    x = Tri.xcor()
    x += 10
    Tri.setx(x)
    Tri.setheading(0)

def Tri_left():
    x = Tri.xcor()
    x -= 10
    Tri.setx(x)
    Tri.setheading(180)

def Tri_green():
    Tri.color("lime green")

def Tri_blue():
    Tri.color("cornflowerblue")
    
def Tri_yellow():
    Tri.color("gold")

def Tri_orange():
    Tri.color("darkorange")

def Tri_violet():
    Tri.color("blueviolet")

def Tri_pink():
    Tri.color("fuchsia")

def Tri_red():
    Tri.color("red")
    

def pen_up():
    Tri.penup()

def pen_down():
    Tri.pendown()
    
#Key assign
win.listen()
#bg
win.onkeypress(bg_black, "2")
win.onkeypress(bg_white, "1")
#movement
win.onkeypress(Tri_up, "Up")
win.onkeypress(Tri_down, "Down")
win.onkeypress(Tri_right, "Right")
win.onkeypress(Tri_left, "Left")
#colors
win.onkeypress(Tri_green, "g")
win.onkeypress(Tri_blue, "b")
win.onkeypress(Tri_yellow, "y")
win.onkeypress(Tri_orange, "o")
win.onkeypress(Tri_violet, "v")
win.onkeypress(Tri_pink, "p")
win.onkeypress(Tri_red, "r")
#ink
win.onkeypress(pen_up, "space")
win.onkeypress(pen_down, "z")

while True:
    win.update()
