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
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

counter_no=sys.argv[1]
cur = db.cursor()
try:
 sql="select queue_id,ticket_no from queue order by queue_id asc limit 0,1";
 cur.execute(sql)
 for row in cur.fetchall():
  print row
 sql= "insert into current_queue(counter_no,ticket_no) values(%s,%s)"
 cur.execute(sql,(counter_no,row[1]))
 cur.execute("delete from queue where queue_id=%s",(row[0])) 
 db.commit()
 mqttc.publish("/queue/call/"+str(counter_no),str(row[1]))

finally:
 db.close()

