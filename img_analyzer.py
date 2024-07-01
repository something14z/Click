from PIL import Image, ImageDraw
img = Image.open('Imgs/to_find.jpg')
colors = dict()
width, height = img.size
pixels = img.load()
for x in range(width):
    for y in range(height):
        color = pixels[x, y]
        if color not in colors:
            colors[color] = {'x':[x], 'y':[y], 'count':0}
        else:
            colors[color]['x'].append(x)
            colors[color]['y'].append(y)
            colors[color]['count'] += 1
main_colors = sorted(colors.keys(), key = lambda x:-colors[x]['count'])




img2 = Image.open('Imgs/yellow.jpg')
colors2 = dict()
width2, height2 = img2.size
pixels2 = img2.load()
for x in range(width2):
    for y in range(height2):
        color = pixels2[x, y]
        if color not in colors2:
            colors2[color] = {'x':[x], 'y':[y], 'count':0}
        else:
            colors2[color]['x'].append(x)
            colors2[color]['y'].append(y)
            colors2[color]['count'] += 1
# new_img = Image.new('RGB', (1000, 1000), (255, 255, 255))
# drawer = ImageDraw.Draw(new_img)
# x = y = 0
# cell_size = 100
# for color in main_colors:
#     print(color)
#     if x >= 1000:
#         x = 0
#         y += cell_size
#     drawer.rectangle((x,y,x+cell_size, y+cell_size),color)
#     drawer.text((x,y),f'{color[0]} {color[1]} {color[2]}')
#     x += cell_size

# new_img.show()
drawer2 = ImageDraw.Draw(img2)
for col in main_colors[:3]:
    xs =colors2[col]['x']
    ys =colors2[col]['y']
    drawer2.rectangle((min(xs),min(ys),max(xs),max(ys)), fill=None, outline=(255,0,0), width=3)
img2.show()
pos = int((min(xs)+max(xs))/2),int((min(ys)+max(ys))/2)