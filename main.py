import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.speed(1)
leonardo.speed(1)
x = random.randrange(1,100)
y = random.randrange(1,100)
michelangelo.forward(x)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(0,10):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# Part B - complete part B here
lst = [3, 4, 6, 9, 12]


for sides in lst:
  
  for i in range(sides):
    leonardo.down()
    leonardo.forward(25)
    leonardo.left(360 / sides)
  leonardo.clear()




window.exitonclick()
