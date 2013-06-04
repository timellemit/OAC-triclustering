from Tkinter import *

root = Tk()
root.title("Whois Tool")

panelFrame = Frame(root, height = 60, bg = 'gray')

impBtn = Button(panelFrame, text = 'Import')
loadBtn = Button(panelFrame, text = 'Start')
visBtn = Button(panelFrame, text = 'Visualize')
saveBtn = Button(panelFrame, text = 'Save')
quitBtn = Button(panelFrame, text = 'Quit')
impBtn.grid(row = 0, column = 0 )
loadBtn.grid(row = 0, column = 1)
visBtn.grid(row = 0, column = 2)
saveBtn.grid(row = 0, column = 3)
quitBtn.grid(row = 0, column = 4)

panelFrame.pack(side = 'top', fill = 'both', expand = 1)

canv = Canvas(root, bg = 'green')
canv.pack(fill = 'both', expand = 1)

text1 = Text(width=30, height=1)
text1.pack(side = 'bottom')

root.mainloop()