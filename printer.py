#! /usr/bin/env python
# -*- coding: utf-8 -*-

from escpos import printer
from PIL import Image, ImageFont, ImageOps, ImageDraw
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="queue")        # name of the data base

#ticket_no=sys.argv[1]
cur = db.cursor()
try:
 sql= "insert into queue_daily(date,total_queue) values(curdate(),1) on duplicate key update total_queue=total_queue+1"
 cur.execute(sql)
 db.commit()
 sql="select total_queue from queue_daily where date=curdate()"
 cur.execute(sql)
 for row in cur.fetchall():
  print row
 sql = "INSERT INTO `queue`(ticket_no,service_type_id) VALUES (%s,%s)"
 cur.execute(sql,(row[0],1))
 db.commit()

 ticketNo=row[0]
 #print out ticket
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
 draw.text((40, 40), str(ticketNo), font=font2)
 waitNo=5
 draw.text((40, 180), u'จำนวนที่รอ : '+str(waitNo)+u' คิว ', font=font3)
 image = ImageOps.invert(image)   # invert image to black on white
 Epson.image(image,impl="bitImageRaster")      # output image to printer
 #Epson.image('footer.png', impl="bitImageRaster",fragment_height=1)
 Epson.text("\n\n\n")


finally:
 cur.close()
 db.close()
