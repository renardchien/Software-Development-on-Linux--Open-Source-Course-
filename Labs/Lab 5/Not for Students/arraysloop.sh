		   #!/bin/bash
		   #Script to show looping. It will take count to 10 using a while loop

		   array1=("one" "two" "three" "four" "five");

		   declare -A array2;
		   array2["juice"]="grape";
		   array2["milk"]="soy";
		   array2["wine"]="white";

		   echo "There are ${#array2[@]} items in array2";

		   for i in "${array1[@]}"		#@ sign meets “at all parameters”
		   do
		   	echo $i;
	 	   done

		   for item in "${!array2[@]}"
		   do
		   	echo ${array2[$item]} $item;
		   done

