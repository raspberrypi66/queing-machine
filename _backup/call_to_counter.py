#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import paho.mqtt.client as mqtt

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="queue")        # name of the data base

def on_connect(mqttc, userdata, flag,rc):
    print("Connected with result code "+str(rc))
    if rc!=0 :
        mqttc.reconnect()

def on_publish(mqttc, userdata, mid):
    print "Published"

def on_disconnect(mqttc, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
        mqttc.reconnect()
    else :
        print "Disconnected successfully"

mqttc=mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_disconnect = on_disconnect
#mqttc.connect("localhost",1883,60)
#mqttc.loop_start()

counter_no=sys.argv[1]
cur = db.cursor()
try:
 sql="select queue_id,ticket_no from queue order by queue_id asc limit 0,1";
 cur.execute(sql)
 for row in cur.fetchall():
  print row
 sql= "insert into current_queue(counter_no,ticket_no) values(%s,%s) on duplicate key update ticket_no=values(ticket_no)"
 cur.execute(sql,(counter_no,row[1]))
 db.commit()
 cur.execute("delete from queue where queue_id=%s",(row[0])) 
 db.commit()
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

