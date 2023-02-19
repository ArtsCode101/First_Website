#!/usr/bin/python 

import sqlite3

import cgi


print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()


username = form.getvalue("user")
password = form.getvalue("pass")


conn = sqlite3.connect('userList.db')

def userTable():
    print("Opened database successfully")
    #conn.execute('''CREATE TABLE userInfo(
    #USER TEXT NOT NULL UNIQUE,
    #PASS TEXT NOT NULL); ''')  # Creates the table
    #conn.commit()
    conn.execute("INSERT INTO userInfo (USER, PASS) \
        VALUES ('aa20bw@brocku.ca', 'FlameLion') ")
    conn.commit()
    conn.close()


def create_user(loginName, password):
	conn = sqlite3.connect('userList.db')
	cursor = conn.cursor()
	params = (username, password)
	cursor.execute ("INSERT INTO userInfo VALUES (?,?)", params)
	conn.commit()
	print('User Creation Successful')
  

create_user(username, password)

conn.commit()
conn.close()


