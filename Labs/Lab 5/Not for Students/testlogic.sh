#!/bin/bash
#Script to test if statements

myNum1=10;
myNum2=”ten”;

if  [ $myNum1 -eq 10 ]
then
echo $myNum1;
else
echo “Num variable did not equal 10”;
fi

echo $1;

if  [ $myNum1 -eq 10000 ]   #-eq means equals for numerical variables
then
	echo “Number is 1000”;
elif  [  $myNum1 -gt 0  ] 	    #-gt means greater than for numerical variables
then
	echo $myNum1;
else
echo “Num variable did not equal 10”;
fi
