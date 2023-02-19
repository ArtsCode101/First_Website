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


def data_delete(loginName, password):
    conn = sqlite3.connect('userList.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userInfo WHERE USER =:loginName AND PASS =:password", {'loginName': loginName, 'password': password})
    row = cur.fetchone()
    if row == None:
        print("User does not exist")
    elif row[0] == loginName and row[1] == password:
        print("User Deletion Successful")
        cur.execute('''DELETE FROM 'userInfo' WHERE USER =:loginName AND PASS =:password''',{'loginName': loginName, 'password': password})
        conn.commit()

data_delete(username, password)
conn.close()

