# -*- coding: utf-8 -*-

import mysql.connector as mysql

conn = mysql.connect(user="root", password="root", host='127.0.0.1')

print(conn)
conn.close()
