#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from escpos import printer
from PIL import Image, ImageFont, ImageOps, ImageDraw
   
   
#get paramenter
queueNo=sys.argv[1]
counterNo=sys.argv[2]



Epson = printer.Usb(0x0fe6,0x811e,0,0x82,0x02)
Epson.set(align='center')
font = ImageFont.truetype('/home/pi/queing-machine/Loma.ttf', 24)
font2 = ImageFont.truetype('/home/pi/queing-machine/Loma.ttf', 96)
font3 = ImageFont.truetype('/home/pi/queing-machine/Loma.ttf', 36)
#box = font.getsize(text)         # work out size of text
# make an image same width as text, but twice the height
#print box[0]
#print box[1]
Epson.image('/home/pi/queing-machine/logo.jpg', impl="bitImageRaster",fragment_height=1)
Epson.text("\n\n")
image = Image.new('RGB', (380, 320))
draw = ImageDraw.Draw(image)
# draw the text at the left edge of the box
draw.text((30, 0), u'ลำดับเลขที่    '   , font=font)
draw.text((40, 40), queueNo, font=font2)
draw.text((40, 180), u'ช่องบริการที่ : '+counterNo, font=font3)
waitNo=5
draw.text((40, 240), u'จำนวนที่รอ : '+str(waitNo)+u' คิว ', font=font)
image = ImageOps.invert(image)   # invert image to black on white
Epson.image(image,impl="bitImageRaster")      # output image to printer
#Epson.image('footer.png', impl="bitImageRaster",fragment_height=1)
Epson.text("\n\n\n")
#Epson.cut()