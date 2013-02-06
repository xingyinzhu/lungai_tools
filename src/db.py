# -*- coding: utf-8 -*-

import sqlite3

#-------------------------------------------------------------------------------
sqlitedb = 'd:/dict/lungai.db'
#-------------------------------------------------------------------------------
def connectsqlite():
    conn = sqlite3.connect(sqlitedb) 
    return conn

#-------------------------------------------------------------------------------

def insertOneWheelIntoDB(conn,imageName='test'):
    cursor = conn.cursor()
    
    
    try:
        cursor.execute("INSERT INTO WHEELS (wheelName,wheelImg) VALUES (?, ?)", (imageName,imageName))
    except sqlite3.Error,e:
        print "SQL Error %s" % (e)
        conn.rollback()
   
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    conn = connectsqlite()
    insertOneWheelIntoDB(conn)
    conn.commit()