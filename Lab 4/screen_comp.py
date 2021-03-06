from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font1 = ImageFont.truetype("Paskowy.ttf", 55)
font2 = ImageFont.truetype("Vermin_Vibes_1989.ttf", 26)
font3 = ImageFont.truetype("GothicPixels.ttf", 25)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

toggleA = False
toggleB = False
color_list = ["#004EFF", "#f5821f", "#2a9d8f", "#ffff00"]
font_list = [font1, font2, font3]
color_index = 0
font_index = 0

while True:
    y = top
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
#     COMMENTING THIS OUT FOR NOW
#     if buttonB.value and not buttonA.value:  # just button A pressed
#         draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#004EFF") # bright blue
#     elif buttonA.value and not buttonB.value:  # just button B pressed
#         draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#f5821f")  # orange
#     else:
#         draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFF00")  # default is bright yellow

    if buttonB.value and not buttonA.value:  # just button A pressed
        color_index += 1
        color_index = color_index % 4
    if buttonA.value and not buttonB.value:  # just button B pressed
        font_index += 1
        font_index = font_index % 3
    
    draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font_list[font_index], fill=color_list[color_index])
        
        
#     if toggleA:
#         draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#004EFF") # bright blue
#     else:
#         draw.text((x, y), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#f5821f")  # orange

    # Display image.
    disp.image(image, rotation)
    sleep(0.05)
