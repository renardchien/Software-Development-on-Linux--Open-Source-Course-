#!/bin/bash

who=`whoami`;

if [ "$who" == "user1" ]
then
	echo "it's user1";
else
	echo "not user1";
fi
