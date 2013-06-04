from Tkinter import *
root = Tk()
frame = Frame(root, height = 360, bg = 'magenta')
for r in range(3):
    for c in range(4):
        Label(frame, text='R%s/C%s'%(r,c),
            borderwidth=1 ).grid(row=r,column=c, sticky = 'w')
            
textFrame = Frame(root, height = 120, width = 600)
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)
textbox = Text(textFrame, font='Arial 14', wrap='word')

scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

canv = Canvas(root, width=300, height=100, bg = 'green')

frame.grid(row = 0, column = 0, sticky = 'n')
canv.grid(row = 1, column = 0)
textFrame.grid(row = 2, column = 0, sticky = 's') 

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)      
root.mainloop()