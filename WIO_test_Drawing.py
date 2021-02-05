import board
import displayio
import time

display = board.DISPLAY

# Create a bitmap with two colors
bitmap = displayio.Bitmap(display.width, display.height, 2)

# Create a two color palette
palette = displayio.Palette(2)
palette[0] = 0x0000ff
palette[1] = 0xff00ff

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)
print("hello")

# Draw a pixel
bitmap[80, 50] = 1

# Draw even more pixels
for x in range(130, 170):
    for y in range(100, 130):
        bitmap[x, y] = 1
        time.sleep(0.01)

while True:
    pass