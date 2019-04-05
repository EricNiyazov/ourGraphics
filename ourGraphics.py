from graphics import *


def draw_rect(X1, Y1, sizeX, sizeY, color, win):
    scrn = Rectangle(Point(X1, Y1), Point(X1 + sizeX, Y1 + sizeY))
    scrn.setFill(color)
    scrn.draw(win)
    
def draw_trap(X1,Y1, sizeX, sizeY, scale, color,win):
    trap = Polygon(Point(X1, Y1), Point(X1+scale, Y1+sizeY), Point(X1+sizeX - scale, Y1+sizeY), Point(X1 + sizeX, Y1))
    trap.setFill(color)
    trap.draw(win)

def draw_key(X1,Y1, sizeX, sizeY, scale, letter, color,win):
    key = draw_trap(X1,Y1, sizeX, sizeY, scale, color,win)
    key = Text(Point(X1 + sizeX / 2, Y1 + sizeY / 2), letter)
    key.draw(win)

##def alphabet_position(text):
##    letr = ('a'='1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
##    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
##    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26')

ABC = ["1","2","3","4","5","6","7","8","9","0","-","Q","W","E","R"
       ,"T","Y","U","I","O","P","[","A","S","D","F","G","H",
       "J","K","L",";","'","Z","X","C","V","B","N","M",",",".","/","sft"
       ]


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

logo = Text(Point(450, 485), "banana")
logo.setText("BANANA")
logo.setTextColor("green")
logo.setSize(30)
logo.setFace("arial")
logo.draw(grwin)

chCol = 230

kX = 250
kY = 470
#letrs = 1
col = "white"
c = 0

print(ABC[3])


for j in range (4):
    kY -= 40
    kX = 250
    
    for i in range (11):
        kX += 30
        draw_key(kX, kY, 30, 37.5, 5, ABC[c], col, grwin)
        print(kX)
        print(kY)
        c += 1
        if (i + j) % 2 == 0:
            col = "dark grey"
        else:
            col = "white"

            
draw_key(400, 250, 100, 37.5, 5, "SPACE","white", grwin)

draw_trap(400, 130, 100, 100, 5, "light grey", grwin)

