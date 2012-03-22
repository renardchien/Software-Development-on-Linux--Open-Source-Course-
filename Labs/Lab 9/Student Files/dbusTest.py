#!/usr/bin/env python

#
# dbusTest.py
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



import gtk 
import dbus
import dbus.service
import gobject
from dbus.mainloop.glib import DBusGMainLoop

#list of songs to return to client
currentSong = ['song1', 'song2', 'song3', 'song4', 'song5']
curPos = 0
#variable to determine if the media player will be visible or not
visible = "off"

#our exported dbus class
class MyTestService(dbus.service.Object):
	#constructor
	def __init__(self):
		#creates a dbus service called org.my.service on the desktop session bus
		bus_name = dbus.service.BusName('org.my.service', bus=dbus.SessionBus())
		#cretes the object name of the service as /org/my/service
		dbus.service.Object.__init__(self, bus_name, '/org/my/service')

	#creates a method in dbus object called hello()
	@dbus.service.method('org.my.service')
	def hello(self):
		return "Hello World"

	#creates a method in dbus object called nextMedia(mType) 
	@dbus.service.method('org.my.service')
	def nextMedia(self, mType):
		global curPos	#grabs the variable curPos in this document instead of making one locally
		if mType == "next":	
			if curPos > 2:	#checks position for array to prevent array from going out of bounds
				curPos = 0
			else:
				curPos = curPos + 1
		

		return currentSong[curPos]	#returns the current song in the array
		
DBusGMainLoop(set_as_default=True) #links this class to the main dbus process loop
myservice = MyTestService()	   #creates a new object of our dbus service class
loop = gobject.MainLoop()	   #adds this class in the main glib loop
loop.run()			   #restarts the main loop



	
