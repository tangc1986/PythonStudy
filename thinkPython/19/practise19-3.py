from swampy.Gui import *

#def make_label():
    #g.la(text='Well Done!')

#def make_buttom():
    #g.bu(text='', command=make_label)
def make_circle():
    global item
    item = canvas.circle([0,0], 100)
   
    
def make_fill():
    color = entry.get()
    item.config(fill=color)

g = Gui()
g.title('Gui')
canvas = g.ca(width=500, height=500)
item = None
button = g.bu(text='Press me.', command=make_circle)
entry = g.en(text='Default text.')
button2 = g.bu(text='Fill Color.', command=make_fill)

item

g.mainloop()
