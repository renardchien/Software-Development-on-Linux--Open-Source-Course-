#!/usr/bin/env python

#
# Map Reduce
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

mapped = []

d = "This is a bunch of words in a doc in a doc"

def mapd(document):
	
	words = document.split()  #gives us each word in array
	
	for word in words:
		mapped.append("%s %s" % (word, 1))


def reduce(findword, mapped):

	total = 0	
	for line in mapped:

		cur_word, num_found = line.split()
		count = int(num_found)

		if cur_word == findword:
			total += count

	print total


mapd(d)
reduce("doc", mapped)
