
import board
import analogio
import displayio
from adafruit_display_text import label
import terminalio
import adafruit_imageload


display = board.DISPLAY
WIDTH = 320
HEIGHT = 240  # Change to 64 if needed
BORDER = 5

textop = 'Hola'
splash = displayio.Group(max_size=10)
display.show(splash)



color_bitmap = displayio.Bitmap(WIDTH , HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH//2 - BORDER * 2, HEIGHT//2 - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x00FF00  # Black

inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)
# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("\lib\cp_sprite_sheet.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create a sprite (tilegrid)
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 1,
                            height = 1,
                            tile_width = 16,
                            tile_height = 16,
                            x=100,
                            y=10)

# Create a Group to hold the sprite
splash.append(sprite)


# Draw a smaller inner rectangle
inner_palette2 = displayio.Palette(1)
inner_palette2[0] = 0x0000FF  # Black
inner_sprite2 = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette2, x=WIDTH//2 + BORDER , y = BORDER)
splash.append(inner_sprite2)

inner_palette3 = displayio.Palette(1)
inner_palette3[0] = 0xFF0000  # Black
inner_sprite3 = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette3, x=BORDER , y = HEIGHT//2 + BORDER)
splash.append(inner_sprite3)

inner_palette4 = displayio.Palette(1)
inner_palette4[0] = 0xFF0077  # Black
inner_sprite4 = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette4, x=WIDTH//2 + BORDER , y = HEIGHT//2 + BORDER)
splash.append(inner_sprite4)

# Draw a label
# text_area = label.Label(terminalio.FONT, text=textop, color=0xFF00FF, x=28, y=HEIGHT // 4 - 1, scale=3)
# splash.append(text_area)
# display.show(splash)

while True:
    pass