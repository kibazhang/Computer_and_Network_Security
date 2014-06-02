#!/usr/bin/env python

### Author: Zaiwei Zhang

###  This is for finding multiplicative inverses using binary
###  GCD arithmetic.    

import sys

if len(sys.argv) != 3:                                                                     
    sys.stderr.write("Usage: %s   <integer>   <modulus>\n" % sys.argv[0])                  
    sys.exit(1) 

a = int( sys.argv[1] )
p = int( sys.argv[2] )

# The following uses Binary GCD arithmetic to find the
# MI of one integer vis-a-vis another integer.
def BGCD(num1, num2):
    temp_num1a, temp_num1b = 1, 0
    temp_num2a, temp_num2b = 0, 1
    MI = 0
    while(~num1 & 1) and (~num2 & 1):
        num1 = num1 >> 1
        num2 = num2 >> 1
        MI += 1
    temp1,temp2 = num1,num2

    while(~num1 & 1):
        num1 = num1 >> 1
        if(~temp_num1a & 1) and (~temp_num1b & 1):
            temp_num1a = temp_num1a >> 1
            temp_num1b = temp_num1b >> 1
        else:
            temp_num1a = (temp_num1a + temp2) >> 1
            temp_num1b = (temp_num1b - temp1) >> 1
    while num1 != num2:
        if(~num2 & 1):
            num2 = num2 >> 1
            if(~temp_num2a & 1) and (~temp_num2b & 1):
                temp_num2a = temp_num2a >> 1
                temp_num2b = temp_num2b >> 1
            else:
                temp_num2a = (temp_num2a + temp2)>> 1
                temp_num2b = (temp_num2b - temp1)>> 1
        elif num2 < num1:
            num1, num2, temp_num1a, temp_num1b, temp_num2a, temp_num2b = num2, num1, temp_num2a, temp_num2b, temp_num1a, temp_num1b
        else:
            num2 = num2 -num1
            temp_num2a = temp_num2a - temp_num1a
            temp_num2b = temp_num2b - temp_num1b
        
    return (2**MI)*num1, temp_num2a, temp_num2b

#Open the output file here
MI,x,y = BGCD(a, p)
FILEOUT = open("mi.txt", "w+")
if MI != 1:
    FILEOUT.write("No multiplicative inverse exists.")
else:
    tempstr = "MI of "+ str(a) + " modulo "+ str(p) + " is: " + str(x)
    FILEOUT.write(tempstr)
FILEOUT.close()
    
Reference: 1.http://www.ucl.ac.uk~ucahcjm/combopt/ext_gcd_python_programs.pdf