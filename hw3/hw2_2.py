from graphics import *

def main():
    win = GraphWin("ball", 500, 500)

    ball = Circle(Point(50, 100), 15)
    ball.setFill("black")

    for i in range(10):
        ball.move(8, -4)

    ball.draw(win)

main()
