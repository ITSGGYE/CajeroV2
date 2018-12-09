# -*- coding: utf-8 -*-

#import mysql.connector as mysql
#import psycopg2 as postgres
from utils.load_json import LoadJson
import logging
import tkMessageBox
from sshtunnel import SSHTunnelForwarder

fileJson = LoadJson().read('parameters.json')

class MySQL:

    def connect(self):

        options = fileJson['mysql']

        db_user = options[0]['user']
        db_password = options[0]['pass']
        db_host = options[0]['host']
        db_port = options[0]['port']
        db_name = options[0]['db']

        ssh_user = options[0]['ssh_user']
        ssh_pass = options[0]['ssh_pass']
        ssh_host = options[0]['ssh_host']
        ssh_port = options[0]['ssh_port']

        general = fileJson['general']

        if general[0]['ssh'] == True:
            try:
                with SSHTunnelForwarder((ssh_host, ssh_port), ssh_password=ssh_pass, ssh_username=ssh_user, remote_bind_address=(db_host, db_port)) as server:
                    conn = mysql.connect(user=db_user, password=db_password, host=db_host, port=db_port, db=db_name)
                    return conn
            except Exception, e:
                tkMessageBox.showerror('Error', e)
        else:

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

        '''try:
            conn = postgres.connect(host=db_host, database=db_name, port=db_port, user=db_user, password=db_password)
            return conn
        except Exception, e:
            tkMessageBox.showerror('Error', e)'''

