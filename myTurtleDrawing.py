'''
Created on Mar 7, 2020

@author: ITAUser
'''
import turtle 

ninja = turtle.Turtle()

ninja.pencolor("blue")

ninja.speed(100)


for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
