from Tkinter import *

SCALE=3

class BoardDisplay:

    def __init__(self, width, height):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.canvas = Canvas(width=SCALE*width, height=SCALE*height, bg='black')
        self.canvas.pack(fill=BOTH, expand=YES)
        self.attention = None
        self.dot = None

    def render_update(self, board):
        if self.dot == None:
            self.dot = drawcircle(self.canvas, board.pos[0], board.pos[1], board.radius, 'white')
            self.attention = drawcircle(self.canvas, board.attention[0], board.attention[1], board.radius, 'red')
        movecircle(self.canvas, self.dot, board.pos[0], board.pos[1], board.radius)
        movecircle(self.canvas, self.attention, board.attention[0], board.attention[1], board.radius)
        self.root.update()

def getcoords(x, y, rad):
    rad += 1
    c = (x-rad, y-rad, x+rad, y+rad)
    return tuple([x * SCALE for x in c])

def movecircle(canvas, circle, x, y, rad):
    bounds = getcoords(x, y , rad)
    canvas.coords(circle, bounds)

def drawcircle(canvas, x, y, rad, color):
    bounds = getcoords(x, y , rad)
    return canvas.create_oval(bounds,width=0,fill='white')
