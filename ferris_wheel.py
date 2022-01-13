import turtle
import turtle as T
import random

t = T.Turtle()
info = T.Turtle()
info.penup()
info.goto(x=-400, y=250)
info.pendown()
t.width(3)
t.color("green")
colors = ["red", "blue", "yellow", "cyan", "black", "purple"]
count = 0
rounds = int(input("Enter the number of rides: "))
for round in range(rounds):
    count += 1
    info.clear()
    info.write(f"No. of round: {count}", font=("Verdana", 15, "normal"), align="left")
    color = random.randint(0, 5)
    t.color(colors[color])
    t.circle(100)

info.clear()
info.write("Hope, you enjoyed the ride", font=("Verdana", 15, "normal"))





turtle.exitonclick()
