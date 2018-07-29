# -*- coding: utf-8 -*-

from mysql.connector import connect


conn = connect(user="root", password="root", host='127.0.0.1')

print(conn)
conn.close()
