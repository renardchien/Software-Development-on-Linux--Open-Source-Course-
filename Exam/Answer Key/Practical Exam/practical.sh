#!/bin/bash

#
# Hello World
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

output="on";
arch="";
built="";

if [ "${1}" = "--no-output" ]
then
	output="off";
elif [ "${1}" = "--only-completion" ]
then
	 output="completion";	
fi


arch=`uname -m`

if [ $arch = "i386" ]
then
	built="32 bit";

elif [ $arch = "i686" ]
then
	built="32 bit";

elif [ $arch = "x86_64" ]
then
	built="64 bit";
else
	built="Unknown Architecture";
fi 



`g++ Hello.cpp -o Hello`;
`javac Hello.java`;
`g++ colorkey.cpp -o colorkey -lSDL -lSDL_image`;

chmod 755 Hello.py;
chmod 755 Hello.pl;


declare -A executions;

executions['C++']=`./Hello`;
executions['Java']=`java Hello`;
executions['SDL']=`./colorkey`;
executions['Python']=`./Hello.py`;
executions['Perl']=`./Hello.pl`;

if [ $output != "off" ]
then
	if [ $output = "on" ]
	then
		for item in "${executions[@]}"
		do
			echo $item;
		done
	
		echo "Built for $built";

	elif [ $output = "completion" ] 
	then
		echo "Built for $built";
	fi

fi
