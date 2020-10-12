# Name: Hunter Monaghan

# greetingCard_HM.py

# Problem: Make objects and put those objects through a loop

# This program will show how graphics.py works when animations are imposed

# Certification of Authenticity:

# Hunter Monaghan

# I certify that this lab is entirely my own work.

# I certify that this lab is my own work, but I

# discussed it with: 

from graphics import*
import random

def delay(d):
    for i in range(d):
        for i in range(1000):
            pass

def greetingCard():

    #
    width = 800
    height = 500
    win = GraphWin("Card", width, height)

    #background color
    win.setBackground(color_rgb(173, 216, 230))


    #Ground
    pt1 = Point(800, 450)
    pt2 = Point(0, 800)
    ground = Rectangle(pt1, pt2)
    
    #flower pink
    flowerPointX = Point(150, 450)
    flowerPointY = Point(150, 430)
    stemFlower = Line(flowerPointX, flowerPointY)
    pedalCenter = Point(150, 430)
    pedal = Circle(pedalCenter, 3)

    #flower blue
    flowerBlueX = Point(600, 450)
    flowerBlueY = Point(600, 433)
    stemBlue = Line(flowerBlueX, flowerBlueY)
    pedalC = Point(600, 430)
    pedalBlue = Circle(pedalC, 4)

    #flower red
    flowerRedX = Point(400, 450)
    flowerRedY = Point(400, 430)
    stemRed = Line(flowerRedX, flowerRedY)
    pedalCent = Point(400, 430)
    pedalRed = Circle(pedalCent, 5)

    #House
    rec = Rectangle(Point(200,360), Point(350,499))
    rec.setFill("White")
    rec.draw(win)

    points = [Point(200,360), Point(350,360), Point(280, 250)]
    triangle = Polygon(points)
    triangle.setFill("brown")
    triangle.draw(win)

    door = Rectangle(Point(280, 500), Point(250, 400))
    door.setFill("red")
    door.draw(win)
    doorKnobCenter = Point(273, 430)
    doorKnob = Circle(doorKnobCenter, 3)
    doorKnob.setFill("black")
    doorKnob.draw(win)

    #Window
    window = Rectangle(Point(310, 325), Point(325, 310))
    window.setFill("silver")
    window.draw(win)
    window2 = window
    window2.clone()
    window2.move(-25, 15)

    #Stars
    pointX = 110
    pointY = 120
    starCenter = Point(pointX, pointY)
    stars = Circle(starCenter, 1)
    stars.setFill("white")
    #stars.setOuline("white")
    stars.draw(win)
    
    
    
    #Sun
    centerY = 150
    centerX = 0
    center = Point(centerX, centerY)
    sun = Circle(center, 50)
    sun.setOutline("orange")
    #sun.move(0,100)
    
    #sun animation
    #dX = 1
   # dY = 1
   # x = True
   # while x == True:
       # d = 350
       # delay(d)
       # sun.move(dX+10, dY+10)
       # dX+=10
        
        
      
        
        
        
        

    #Colors
    sun.setFill(color_rgb(255, 255, 51))#yellow
    ground.setFill(color_rgb(143, 188, 143))
    pedal.setFill("Pink")
    pedalBlue.setFill("Blue")
    pedalRed.setFill("red")

    #Text
    Exit = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    
    #Output
    ground.draw(win)
    stemFlower.draw(win)
    stemBlue.draw(win)
    stemRed.draw(win)
    pedal.draw(win)
    pedalRed.draw(win)
    pedalBlue.draw(win)
    sun.draw(win)
    Exit.draw(win)
    win.getMouse()
    win.close()



    
greetingCard()
