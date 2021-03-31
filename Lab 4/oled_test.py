# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from time import strftime, sleep
import board
import busio
import adafruit_ssd1306
import adafruit_mpu6050
from PIL import Image, ImageDraw, ImageFont

BORDER = 5

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create mpu object
mpu = adafruit_mpu6050.MPU6050(i2c)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example for details
def draw_circle(xpos0, ypos0, rad, col=1):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        oled.pixel(xpos0 + x, ypos0 + y, col)
        oled.pixel(xpos0 + y, ypos0 + x, col)
        oled.pixel(xpos0 - y, ypos0 + x, col)
        oled.pixel(xpos0 - x, ypos0 + y, col)
        oled.pixel(xpos0 - x, ypos0 - y, col)
        oled.pixel(xpos0 - y, ypos0 - x, col)
        oled.pixel(xpos0 + y, ypos0 - x, col)
        oled.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)


# initial center of the circle
center_x = 63
center_y = 15
# how fast does it move in each direction
x_inc = 1
y_inc = 1
# what is the starting radius of the circle
radius = 8

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()
while True:
#     # undraw the previous circle
#     draw_circle(center_x, center_y, radius, col=0)

#     # if bouncing off right
#     if center_x + radius >= oled.width:
#         # start moving to the left
#         x_inc = -1
#     # if bouncing off left
#     elif center_x - radius < 0:
#         # start moving to the right
#         x_inc = 1

#     # if bouncing off top
#     if center_y + radius >= oled.height:
#         # start moving down
#         y_inc = -1
#     # if bouncing off bottom
#     elif center_y - radius < 0:
#         # start moving up
#         y_inc = 1

#     # go more in the current direction
#     center_x += x_inc
#     center_y += y_inc

#     # draw the new circle
#     draw_circle(center_x, center_y, radius)
#     # show all the changes we just made

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white background
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

    # Draw a smaller inner rectangle
    draw.rectangle(
        (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
        outline=0,
        fill=0,
    )

    # Load default font.
    font = ImageFont.load_default()
       

    # Draw Some Text
    text = mpu.acceleration
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
    )

    # Display image
    oled.image(image)
    
    
    
    oled.show()
