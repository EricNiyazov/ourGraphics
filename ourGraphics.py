from graphics import *


def draw_rect(X1, Y1, sizeX, sizeY, color, win):
    scrn = Rectangle(Point(X1, Y1), Point(X1 + sizeX, Y1 + sizeY))
    scrn.setFill(color)
    scrn.draw(win)


grwin = GraphWin("ourGraphics.py", 1500, 1000)
grwin.setCoords(0, 0, 1000, 1000)


draw_rect(230, 500, 440, 433, "dark blue", grwin)

draw_rect(250, 500, 400, 403, "black", grwin)

trap = Polygon(Point(180, 105), Point(180+50, 105+395), Point(180+540 - 50, 105+395), Point(180 + 540, 105))
trap.setFill("black")
trap.draw(grwin)
