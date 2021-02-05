import board
import displayio
import terminalio
import time
from adafruit_display_text import label

display = board.DISPLAY
WIDTH = 320
HEIGHT = 240  # Change to 64 if needed
BORDER = 5

# Make the display context
splash = displayio.Group(max_size=10)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF44FF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x004400  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFF00FF, x=28, y=HEIGHT // 2 - 1)
splash.append(text_area)
display.show(splash)
while True:
    pass