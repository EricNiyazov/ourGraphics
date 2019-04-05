from graphics import *


def draw_rect(X1, Y1, sizeX, sizeY, color, win):
    scrn = Rectangle(Point(X1, Y1), Point(X1 + sizeX, Y1 + sizeY))
    scrn.setFill(color)
    scrn.draw(win)
    
def draw_trap(X1,Y1, sizeX, sizeY, scale, color,win):
    trap = Polygon(Point(X1, Y1), Point(X1+scale, Y1+sizeY), Point(X1+sizeX - scale, Y1+sizeY), Point(X1 + sizeX, Y1))
    trap.setFill(color)
    trap.draw(win)

grwin = GraphWin("ourGraphics.py", 1500, 1000)
grwin.setCoords(0, 0, 1000, 1000)


draw_rect(230, 500, 440, 433, "dark blue", grwin)

draw_rect(250, 500, 400, 403, "black", grwin)


draw_trap(180, 105, 540, 395, 50, "black", grwin) 

draw_trap(200,125,500, 375, 50, "grey", grwin)

draw_rect(255, 505, 390, 392, "light blue", grwin)

draw_rect(300, 700, 75, 100, "red", grwin)
draw_rect(300, 590, 75, 100, "blue", grwin)
draw_rect(385, 700, 75, 100, "green", grwin)
draw_rect(385, 590, 75, 100, "yellow", grwin)

