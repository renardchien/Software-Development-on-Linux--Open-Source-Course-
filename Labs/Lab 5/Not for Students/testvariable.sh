#!/bin/bash

variable3="yes";

variable4="I'm a variable";
export variable4;

if [ "$variable2" = "" ]
then
	variable2="maybe";
	export variable2;
	echo "exported new variable 2";
	bash echovars.sh;
else
	echo "not empty";
fi

myNum1=10;

if [ "$myNum1" -eq 10 ]
then
	echo $myNum1;
else
	echo "wrong";
fi
