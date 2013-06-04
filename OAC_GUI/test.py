
from Tkinter import *
root=Tk()
frame = Frame(root, bg = 'gray')
#textFrame = Frame(root, height = 40, width = 600, bg = 'yellow') 
textbox = Text(frame,font='Arial 14', wrap='word')
textbox.config( height = 40, width = 40)
canv = Canvas(frame, width=300, height=100, bg = 'green')

impBtn = Button(frame, text = 'Import')
loadBtn = Button(frame, text = 'Start')
visBtn = Button(frame, text = 'Visualize')
saveBtn = Button(frame, text = 'Save')
quitBtn = Button(frame, text = 'Quit')
    
#impBtn.bind("<Button-1>", ImpFile)
#loadBtn.bind("<Button-1>", StartCalc)
#visBtn.bind("<Button-1>", Visualize)
#saveBtn.bind("<Button-1>", SaveFile)
#quitBtn.bind("<Button-1>", Quit)
    
#impBtn.place(x = 10, y = 10, width = 50, height = 40)
#loadBtn.place(x = 70, y = 10, width = 50, height = 40)
#visBtn.place(x = 130, y = 10, width = 80, height = 40)
#saveBtn.place(x = 220, y = 10, width = 40, height = 40)
#quitBtn.place(x = 270, y = 10, width = 40, height = 40)

impBtn.grid(row = 0, column = 0, sticky = 'w')
loadBtn.grid(row = 0, column = 1, sticky = 'w')
visBtn.grid(row = 0, column = 2, sticky = 'w')
saveBtn.grid(row = 0, column = 3, sticky = 'w')
quitBtn.grid(row = 0, column = 4, sticky = 'w')

canv.grid(row=1, column=0, columnspan = 5)
textbox.grid(row=2, column=0, columnspan = 5)

frame.grid()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()