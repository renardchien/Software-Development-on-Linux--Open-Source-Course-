#!/usr/bin/env python

#
# couchTest.py
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

import couchdb
from couchdb.client import Server

#This connects to the couchdb server
server = Server('http://127.0.0.1:9999/')
print 'Connected Established'

try:
	#This creates a database in couchdb called gamedb
	#Database names must be lowercase, but table/document names do not need to be
	db = server.create('gamedb')
	print 'database created'
except:
	#In the case the database already exists we will delete it and start a new one
	del server['gamedb']
	db = server.create('gamedb')
	print 'database deleted and created'

#Creating JSON object data, db is your database, while 'character#' is the table name you will be assigning. 
#The dictionary holds a variable you are adding and it's value. IE: uid is the variable and 1 is the value. 
#Python will automatically change this to a json object for you when it writes to the database
db['character1'] = dict(uid=1, level=12, name='py')
db['character2'] = dict(uid=2, level=25, name='thon')
db['character3'] = dict(uid=3, level=30, name='three')

#this is how you build a query, the query is exported javascript
#the first part of the emit statement is the key and the second is the value (array of attributes)
queryString = '''function(doc) 
		{ 
			if ( doc._id == "character2" ) 
			{ 
				emit(doc._id, [doc.uid, doc.level, doc.name]); 
			}
		}'''

#runs query and gets results
results = db.query(queryString)

print "Results Found: ", len(results)

#printing the key and value returned from our javascript query
for result in results:
	print "Key used: ", result.key, "\tValue: ", result.value


###Updating an entry
#First get the document by name, then update the doc by name and give it a new value, then save it
doc = db.get('character2')
doc['level'] = int(doc['level']) + 1
db.save(doc)		

#reruns query and gets results
results = db.query(queryString)

#The update command modifies any documents we are looking at.
print "\nAfter Update"
for result in results:
	print "Key used: ", result.key, "\tValue: ", result.value
