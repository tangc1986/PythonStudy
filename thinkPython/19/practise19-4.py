from swampy.Gui import *
from Tkinter import PhotoImage
import PIL.Image
import PIL.ImageTk

g = Gui()
canvas = g.ca(width=300)
photo = PhotoImage(file='danger.gif')
canvas.image([0,0], image=photo)

g.la(image=photo)
g.bu(image=photo)

image = PIL.Image.open('allen.png')
photo2 = PIL.ImageTk.PhotoImage(image)
g.la(image=photo2)


g.mainloop()
