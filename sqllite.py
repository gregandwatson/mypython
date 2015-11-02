#!/usr/bin/python

import os
import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("INSERT  INTO People VALUES('Greg', 'Greenlee', 43)")
connection.commit()
