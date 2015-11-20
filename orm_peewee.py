#!/usr/bin/env python
__author__ = 'Jack'

# pip install peewee
from playhouse.sqlite_ext import SqliteExtDatabase


db = SqliteExtDatabase('my_peewee_database.db')


