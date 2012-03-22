#!/bin/bash

echo "Number is ${1}";
echo ${2};
echo ${3};

if  [ "${1}" == "one" ]   #-eq means equals for numerical variables
then
	echo "Number is ${1}";
elif  [  -z ${1}  ] 	    #-gt means greater than for numerical variables
then
	echo "Number is empty";
else
	echo "Number was not one and was not empty";
fi
