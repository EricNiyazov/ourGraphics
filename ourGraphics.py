from graphics import *

grwin = GraphWin("ourGraphics.py", 1500, 1000)
grwin.setCoords(0, 0, 1000, 1000)


scrn1 = Rectangle(Point(230, 500), Point(230 + 440, 500 + 433))
scrn1.setFill("dark blue")
scrn1.draw(grwin)

scrn = Rectangle(Point(250, 500), Point(250 + 400, 500 + 403))
scrn.setFill("grey")
scrn.draw(grwin)


draw_rect(230, 500, 440, 433, "dark blue", grwin)
