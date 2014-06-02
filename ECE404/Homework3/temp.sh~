for ((I=10000;I<20000;I++))
do 
    python Zhang_prime.py $I
    temp=$(more prime.txt)
    temp_Arr=($temp)
    ((check=1))
    for ((J=0;J<${#temp_Arr[*]};J++))
    do
	if [[ ${temp_Arr[$J]} == 'not' ]]
	then
	    ((check=0))
	fi
    done
    if ((check == 1))
    then
	echo "Found a prime number:" ${temp_Arr[0]}
    fi
done
