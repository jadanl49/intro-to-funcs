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
    for i in range(60):
     t.speed(0)
     t.forward(x)
     t.left(y) 
square(100,90) 


           
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)  

