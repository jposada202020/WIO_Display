import board
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

display = board.DISPLAY

# Set text, font, and color
text = "Hello World!"
font = bitmap_font.load_font("/fonts/Helvetica-Bold-16.bdf")
color = 0xFF00FF

# Create the text label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 100
text_area.y = 80

# Show it
display.show(text_area)

# Loop forever to prevent code from exiting
while True:
    pass