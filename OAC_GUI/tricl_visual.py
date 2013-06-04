from Tkinter import *

class Rect(object):
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        coord = self.getCoordinates()
        self.rect = self.canvas.create_rectangle(coord[0], coord[1],
                                                 coord[2], coord[2],
                                                 fill="blue")
        
class App(object):

    def __init__(self, root, width=256, height=256):
        self.width = width
        self.height = height

        self.root = root
        self.root.title("tkinter_test01")
        self.root.geometry("%sx%s"%(self.width, self.height))

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        # Bind the event to move our Rect:
        self.canvas.bind("<Motion>", self.moveRect)
        self.canvas.pack()

        # Create our Rect object:
        self.rect = Rect(self.canvas, 32, 32)

        self.root.mainloop()

    def moveRect(self, event):
        # Callback that will move our Rect object
        self.rect.move(event.x, event.y)