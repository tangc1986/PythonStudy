from swampy.Gui import *

def make_label():
    g.la(text='Well Done!')

def make_buttom():
    g.bu(text='', command=make_label)

g = Gui()
g.title('Gui')

button = g.bu(text='Press me.', command=make_buttom)
g.mainloop()
