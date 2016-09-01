from swampy.World import World

def draw_rectangle(canvas, rectangle):
    bbox = [[rectangle.corner.x,                 rectangle.corner.y], 
            [rectangle.corner.x+rectangle.width, rectangle.corner.y+rectangle.height]]
    canvas.rectangle(bbox)




world = World()
canvas = world.ca(width=500, height=500, background='white')
#bbox = [[-150, -100], [150, 100]]
#canvas.rectangle(bbox, outline='black', width=2, fill='green4')
#canvas.circle([-25,0], 70, outline=None, fill='red')

points = [[-150,-100], [150,100], [150,-100]]
canvas.polygon(points, fill='blue')

world.mainloop()