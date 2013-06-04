from Tkinter import *
from button_events import *
from random import random

def clusterVisual(canvas, tbox, cont, Tricl):
    global context, textbox, Triclusters, freqDict, highlighted_tricls
    context, textbox, Triclusters = cont, tbox, Tricl
    freqDict = {}
    highlighted_tricls = []
    for tricl in Tricl.values():
        for u in tricl[0]:
            for t in tricl[1]:
                if (u,t) in freqDict.keys():
                    freqDict[(u,t)] += 1
                else:
                    freqDict[(u,t)] = 1
    #print freqDict
    max_frequency = max(freqDict.values()) 
    canvas.config(width = 400, height = 200)
    clusterFrame = Frame(canvas, width = 800, height = 600)
    for x in xrange(cont.user_num):
        for y in xrange(cont.tag_num):
            if (x,y) in freqDict.keys():
                relat_freq = float(freqDict[(x,y)])/max_frequency
                color = '#%02x%02x%02x' % (0.5*255*(2-relat_freq), 1, 1) 
            else:
                color = 'gray'
            btn = Button(clusterFrame, bg = color)
            #btn.gri
            btn.bind("<Button-1>", button_event_left)
            btn.bind("<Button-3>", button_event_right)
            btn.grid(column=y, row=x, sticky = 'news')
        label = Label(clusterFrame, text = str(cont.U[x]), \
                      bg = '#%02x%02x%02x' % (255, 168, 88) ) 
        label.grid(column=cont.user_num+1, row=x, sticky = 'news')
    # tag labels
    for y in xrange(cont.tag_num):
        label = Label(clusterFrame, text = str(cont.T[y]), \
                      bg = '#%02x%02x%02x' % (255, 168, 88) ) 
        label.grid(column=y, row=cont.tag_num, sticky = 'news')
    # corner label 
    label = Label(clusterFrame, text = 'T\U', \
                      bg = '#%02x%02x%02x' % (255, 168, 88) ) 
    label.grid(column=cont.user_num+1, row=cont.tag_num, sticky = 'news')  
    for x in xrange(cont.user_num):
        Grid.columnconfigure(clusterFrame,x,weight=1)
    for y in xrange(cont.tag_num):
        Grid.rowconfigure(clusterFrame,y,weight=1)
    clusterFrame.pack(side = 'bottom', expand = 1)
    Grid.rowconfigure(clusterFrame,7,weight=1)
    Grid.columnconfigure(clusterFrame,0,weight=1) 
    global btn_dict
    btn_dict = button_dict(clusterFrame)
    
def button_event_left(ev):
    btn_grid_info_dict = ev.widget.grid_info()
    user, tag = int(btn_grid_info_dict['row']), int(btn_grid_info_dict['column'])
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', context.list_tricls_by_triconcepts(user, tag, Triclusters))
    #print ev.widget.master.children

def button_event_right(ev):
    btn = ev.widget
    btn_grid_info_dict = btn.grid_info()
    user, tag = int(btn_grid_info_dict['row']), int(btn_grid_info_dict['column'])
    
        
    def list_tricl():
        textbox_triclusters(context.list_triclusters(user, tag, Triclusters))
        
    def highlight_biggest_tricl():
        biggest_tricl = context.biggest_tricl(user, tag, Triclusters)
        highlighted_tricls.append(biggest_tricl)
        users, tags = biggest_tricl[0], biggest_tricl[1]
        random_color = '#%02x%02x%02x' % (160*random(),120*random(),80*random()) 
        for (x,y) in [(u,t) for u in users for t in tags]:
            
            btn_dict[(x,y)].configure(bg = random_color)
        textbox.delete('1.0', 'end') 
        textbox.insert('1.0', 'Highlighted tricluser: ' + str(biggest_tricl))
        print highlighted_tricls
        
    def list_triconcepts():
        textbox.delete('1.0', 'end') 
        textbox.insert('1.0', context.list_triconcepts(user, tag))
                
    def clear_highlight():
        
        for tricl in highlighted_tricls:
            users, tags  = tricl[0], tricl[1]
            for (x,y) in [(u,t) for u in users for t in tags]:
                max_frequency = max(freqDict.values()) 
                if (x,y) in freqDict.keys():
                    relat_freq = float(freqDict[(x,y)])/max_frequency
                    color = '#%02x%02x%02x' % (0.5*255*(2-relat_freq), 1, 1) 
                else:
                    color = 'gray'
                btn_dict[(x,y)].configure(bg = color)
        textbox.delete('1.0', 'end') 
        
             
    menu = Menu(btn, tearoff=0)
    menu.add_command(label="Triclusters", command = list_tricl)
    menu.add_command(label="Highlight biggest", command = highlight_biggest_tricl)
    menu.add_command(label="Triconcepts", command = list_triconcepts)
    menu.add_command(label="Clear highlight", command = clear_highlight)
    menu.post(ev.x_root, ev.y_root)

def button_dict(btn_frame):
    button_dict = {}
    button_dict0 = btn_frame.children
    for btn in button_dict0.values():
        btn_x, btn_y = int(btn.grid_info()['row']), int(btn.grid_info()['column'])
        button_dict[(btn_x, btn_y)] = btn
    return button_dict

def textbox_triclusters(Tricls):
    textbox.delete('1.0', 'end') 
    for tricl in Tricls:
        textbox.insert('1.0', str(context.present_tricl(tricl)) + '\n')