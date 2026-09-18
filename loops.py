import turtle
from turtle import *
t = Turtle()
t.shape('turtle')



# for i in range(61):
#     t.speed(0)
#     t.forward(100)
#     t.left(90)   
#     t.forward(100)   
#     t.left(90)    
#     t.forward(100)
#     t.left(90)
#     t.forward(100)        
#     t.left(90)
#     t.left(5
def square(x,y):
    t.left(5)
    for i in range(5):
     t.speed(0)
     t.forward(x)
     t.left(y) 
square(5,144) 

# def doubleSquares(iRange):
#     length = 25    
#     for i in range(iRange):
#      square(length, 90)
#     length = length * 0.5
# doubleSquares(5)
def addSquares(iRange):
     length = 5
     for i in range(iRange):
         square(length, 144)
         length += 5
addSquares(60) 

turtle.done()



