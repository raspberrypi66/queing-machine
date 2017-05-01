#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import paho.mqtt.client as mqtt

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="queue")        # name of the data base

mqttc=mqtt.Client()
#mqttc.connect("localhost",1883,60)
#mqttc.loop_start()

counter_no=sys.argv[1]
cur = db.cursor()
try:
 sql="select counter_no,ticket_no from current_queue where counter_no=%s";
 cur.execute(sql,(counter_no))
 for row in cur.fetchall():
  print row
 try:
  mqttc.connect("localhost",1883,60)
  mqttc.loop_start()
  mqttc.publish("/queue/call/"+str(counter_no),str(row[1]),1)
 except Exception as e:
  print "unexpected mqtt problem"
except Exception as e:
  print "unexpected mysql problem"

finally:
 cur.close()
 db.close()
 mqttc.disconnect()


