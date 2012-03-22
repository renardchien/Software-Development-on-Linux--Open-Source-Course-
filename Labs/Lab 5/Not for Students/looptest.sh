#!/bin/bash
#Script to show looping. It will take count to 10 using a while loop

counter=0;
while [ $counter -lt 5 ];
do
echo $counter;
let counter=counter+1;	#the let command allows you to do arithmetic on 								#variables
done

until [ $counter -eq 0 ];
do
echo $counter;
let counter=counter-1;
done

