import turtle
import math
import random

def drawSpiros(x, y, R, r, l):
    k = r/R
    revol = r//math.gcd(R, r)
    a = 0.0
    px = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    py = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
    turtle.pencolor(random.choice(color))
    turtle.up()
    turtle.setpos(x + px , y + py)
    turtle.down()


    for i in range(0, 360 * revol + 1, 5):
        a = math.radians(i)
        px = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        py = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        turtle.setpos(px + x, py + y)
        if i % 360 == 0:
            turtle.pencolor(random.choice(color))
    turtle.clear()
    value = random.randrange(21)
    drawSpiros(50, 50, 220, 65, value/10)

value = random.randrange(21)

drawSpiros(50, 50, 220, 65 , value/10)

turtle.mainloop()