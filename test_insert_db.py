#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="queue")        # name of the data base

cur = db.cursor()
try:
 sql= "insert into queue_daily(date,total_queue) values(curdate(),1) on duplicate key update total_queue=total_queue+1"
 cur.execute(sql)
 db.commit()
 sql="select total_queue from queue_daily where date=curdate()"
 cur.execute(sql)
 for row in cur.fetchall():
  print row
 db.commit()

finally:
 cur.close()
 db.close()
