#!/usr/bin/env python
__author__ = 'Jack'

import sqlite3
import os.path


def Main():
    mypath = './'
    dbname = 'myfirstsqlite.db'
    try:
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

    except sqlite3.Error:
        if conn:
            print("Error! Rolling back")
            conn.rollback()
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    Main()

