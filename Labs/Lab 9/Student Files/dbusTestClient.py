#!/usr/bin/env python

#
# dbusTestClient.py
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

import dbus

#grabs the current desktop session
bus = dbus.SessionBus()

#grabs an object of dbus itself. This is useful when you want to see what is currently running on dbus 
remote = bus.get_object("org.freedesktop.DBus", "/org/freedesktop/DBus")

#prints all of the methods available from an object
#print remote.Introspect()

#interfaces with our dbus object so we can see everything currently running on dbus
iface = dbus.Interface(remote, 'org.freedesktop.DBus')
#prints all of the current running objects on dbus
#print iface.ListNames()

#gets an object of our dbusTest.py service
testService = bus.get_object('org.my.service', '/org/my/service')

#calls the hello method from our testService bus object 
print testService.hello()

#you may also alias functions in dbus instead of calling them directly
#grabs the method nextMedia from our dbusTest.py service and aliases it to nextSong
nextSong = testService.get_dbus_method('nextMedia', 'org.my.service')
print nextSong("next")

#creates an object of banshee media player
banshee = bus.get_object('org.bansheeproject.Banshee', '/org/bansheeproject/Banshee/ClientWindow')
visible = "off"
if visible == "on":
	#calls banshee to make the media player visible
	banshee.Present()
else:
	#calls banshee to make the media player invisible 
	banshee.Hide()
