#!/usr/bin/env python

###  script for calculate the prime number less than 20000
###  Zaiwei Zhang
###  Feb 5, 2014
    
import os, sys

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
    
FOUT = open("tempout.txt", "w+")
for i in range(10000, 20000):
    check = findPrime(i)
    if check == 1:
        tempstr = "Found a prime number: "+str(i)+"\n"
        FOUT.write(tempstr)
    
FOUT.close()