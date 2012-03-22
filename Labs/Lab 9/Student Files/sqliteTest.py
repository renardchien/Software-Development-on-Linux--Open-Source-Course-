#!/usr/bin/env python

#
# sqliteTest.py
#
# Copyright 2012 Cody Van De Mark
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either 
# version 3.0 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public 
# License along with this library.  If not, see <http://www.gnu.org/licenses/>.
# 
##

import sqlite3

#The path is where you want the database to be stored
#You may also use ':memory:' if you just want the database to exist temporarily in ram
conn = sqlite3.connect('/tmp/media')

#A cursor is a pointer to the current database. You can make your changes to the cursor without committing them to the database
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS pictures''')

#this adds a query to the cursor to execute
cursor.execute('''CREATE TABLE pictures (
		id INT primary key, 
		name TEXT, 
		type VARCHAR(5), 
		height INT, 
		width INT)''') 

#inserting a single row
cursor.execute('''INSERT INTO pictures VALUES (1, "pic1", ".png", 1024, 768) ''')

#mass insert, question marks are used to prevent sql injection of data coming from variables
#question marks are a must for security of anything that is not hard coded
for dataList in [(2, "pic2", ".jpg", 150, 150),
		 (3, "pic3", ".png", 1024, 768),
		 (4, "pic4", ".png", 700, 500)
		]:
	cursor.execute('INSERT INTO pictures VALUES(?,?,?,?,?)', dataList)

#this commits the cursor changes to the database
conn.commit()

cursor.execute('''SELECT * FROM pictures''')

#because the cursor points to a place in the database, it automatically holds your query results when it executes the query
for row in cursor:
	print row

#this closes the cursor 
cursor.close() 
conn.close()
