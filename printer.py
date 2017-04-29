#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="queue")        # name of the data base
ticket_no=sys.argv[1]
cur = db.cursor()
try:
 sql = "INSERT INTO `queue`(ticket_no,service_type_id) VALUES (%s,%s)"
 cur.execute(sql,(ticket_no,1))
 db.commit()

finally:
 db.close()
