#!/usr/bin/python 

import sqlite3

import cgi

import webbrowser

form = cgi.FieldStorage()

username = form.getvalue("user")
password = form.getvalue("pass")

print("Content-Type: text/html\n\n")

conn = sqlite3.connect('userList.db')


def userTable():
    conn.execute('''CREATE TABLE userInfo(
    USER TEXT NOT NULL UNIQUE,
    PASS TEXT NOT NULL); ''')  # Creates the table
    conn.commit()
    conn.execute("INSERT INTO userInfo (USER, PASS) \
        VALUES ('aa20bw@brocku.ca', 'FlameLion') ")
    conn.commit()
    conn.close()


def data_retrival(loginName, password):
    conn = sqlite3.connect('userList.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM userInfo WHERE USER=:loginName''',{'loginName': loginName})
    row = cur.fetchone()
    if row is None:
        print("login failed")
    elif row[1] == password:
        print("Login Successful")   
    else:
        print("invalid password") 



data_retrival(username, password)




