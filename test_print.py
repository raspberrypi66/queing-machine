#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from escpos import printer
from PIL import Image, ImageFont, ImageOps, ImageDraw
   
   

Epson = printer.Usb(0x0fe6,0x811e,0,0x82,0x02)
Epson.set(align='center')
font = ImageFont.truetype('/home/pi/queing-machine/Loma.ttf', 24)

Epson.image('/home/pi/queing-machine/logo.jpg', impl="bitImageRaster",fragment_height=1)
Epson.text("\n\n")
image = Image.new('RGB', (380, 320))
draw = ImageDraw.Draw(image)
# draw the text at the left edge of the box
draw.text((40, 0), "Hello World!", font=font)
image = ImageOps.invert(image)   # invert image to black on white
Epson.image(image,impl="bitImageRaster")      # output image to printer
Epson.text("\n\n\n")
