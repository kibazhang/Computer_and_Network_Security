#!/usr/bin/env python

### Author: Zaiwei Zhang

###  This is for finding all the prime numbers before input n.

import sys

if len(sys.argv) != 2:                                                                     
    sys.stderr.write("Usage: %s   <integer>\n" % sys.argv[0])                  
    sys.exit(1) 

n = int( sys.argv[1] )

def MI(num, mod):
    NUM = num; MOD = mod
    x, x_old = 0L, 1L
    y, y_old = 1L, 0L
    while mod:
        q = num // mod
        num, mod = mod, num % mod
        x, x_old = x_old - q * x, x
        y, y_old = y_old - q * y, y
    if num != 1:
        return 0
    else:
        MI = (x_old + MOD) % MOD
        return MI

def findPrime(number):
    test = 1
    check = 1
    while test < number:
        temp = MI(test, number)
        if temp == 0:
            check = 0
            break
        else:
            pass
        test += 1
    return check
                        

check = findPrime(n)
FOUT = open("prime.txt", "w+")
if check == 1:
    temp_string = sys.argv[1] + " is a prime number."
    FOUT.write(temp_string)
    FOUT.close()
    sys.exit(2)
else:
    temp_string = sys.argv[1] + " is not a prime number."
    FOUT.write(temp_string)
    FOUT.close()
    sys.exit(3)



