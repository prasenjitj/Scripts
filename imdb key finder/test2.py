#!/usr/bin/python
# -*- coding: utf-8 -*-

# import re
# import csv
# from googleapiclient.discovery import build
import mysql.connector
# from mysql.connector import Error
# apikeys = ['AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ','AIzaSyCv6pMQ4ObhFbtWuM5Ge5CEmLZ5o_VcuXQ','AIzaSyB7BqsM_vljNSPOq4twbB7N3sUutyjoobE']

conn = mysql.connector.connect(host='localhost',database='test',user='root',password='')
print('Connected to MySQL database')
cursor = conn.cursor()
cursor.execute("SELECT * FROM api")
rows = cursor.fetchall()

keycount = 0
keys = 1
key_id =''


keycount += 1
if keycount == 81:
	keycount = 1
if keycount == 1:
	keys	+= 1
	for i in rows:
		key_id = i[1]
		print key_id

 
conn.close()
 
