from visual import *

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)

#color = (0.1, 0.1, 0.9)
#sphere(pos=scene.center, radius=128, color=color)

#t = range(0, 256, 51)
#for x in t:
    #for y in t:
        #for z in t:
            #pos = x, y, z
            #each_color = (x/255, y/255, z/255)
            #sphere(pos=pos, radius=10, color=each_color)
import color_list

for k, color in color_list.read_colors()[0].items():
    if k.strip() != '':
        x = int(color[1:1+2], 16)
        y = int(color[1+2:1+2+2], 16)
        z = int(color[1+2+2:1+2+2+2], 16)
        pos = (x, y, z)
        each_color = (x/255, y/255, z/255)
        sphere(pos=pos, radius=10, color=each_color)