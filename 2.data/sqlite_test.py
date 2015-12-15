#!/usr/bin/env python
__author__ = 'Jack'

import sqlite3
import os.path

mypath = './'
dbname = 'myfirstsqlite.db'

if not os.path.exists(mypath + dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE fruit
                (name TEXT, calories INT, price NUMERIC)
                 """)
    print('db created')

conn = sqlite3.connect(dbname)
cursor = conn.cursor()

fruit = [('banana', '30', '0.5'),
         ('pinapple', '12', '100'),
         ('kiwi', '10', '1.1')]
cursor.executemany('INSERT INTO fruit VALUES(?,?,?)', fruit)
conn.commit()

sql = "SELECT * FROM fruit WHERE name=?"
cursor.execute(sql, ["kiwi"])
print(cursor.fetchall())
