# -*- coding: utf-8 -*-

import mysql.connector as mysql
import psycopg2 as postgres
from utils.load_json import LoadJson
import logging
import tkMessageBox


class MySQL:

    def connect(self):

        fileJson = LoadJson().read('parameters.json')
        options = fileJson['mysql']

        db_user = options[0]['user']
        db_password = options[0]['pass']
        db_host = options[0]['host']
        db_port = options[0]['port']
        db_name = options[0]['db']
        try:
            conn = mysql.connect(user=db_user, password=db_password, host=db_host, port=db_port, db=db_name)
            return conn
        except Exception, e:
            tkMessageBox.showerror('Error', e)


class PostgreSQL:

    def connect(self):
        fileJson = LoadJson().read('parameters.json')
        options = fileJson['postgres']

        db_user = options[0]['user']
        db_password = options[0]['pass']
        db_host = options[0]['host']
        db_port = options[0]['port']
        db_name = options[0]['db']

        try:
            conn = postgres.connect(host=db_host, database=db_name, port=db_port, user=db_user, password=db_password)
            return conn
        except Exception, e:
            tkMessageBox.showerror('Error', e)

