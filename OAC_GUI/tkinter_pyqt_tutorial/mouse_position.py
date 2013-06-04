import Tkinter

class App:
    def __init__(self, root):
        f = Tkinter.Frame(width=100, height=100, background="bisque")
        f.pack(padx=100, pady=100)
        f.bind("<1>", self.OnMouseDown)

    def OnMouseDown(self, event):
        print "frame coordinates: %s/%s" % (event.x, event.y)
        print "root coordinates: %s/%s" % (event.x_root, event.y_root)

root=Tkinter.Tk()
app = App(root)
root.mainloop()