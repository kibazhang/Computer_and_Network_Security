#!/usr/bin/env python

##  Zhang_hw06.py
##  Author: Zaiwei Zhang
##  Date: March 3, 2014

from BitVector import*
from PrimeGenerator import PrimeGenerator as pg
import sys
#from math import*

e = 65537

#To get the gcd of a and b
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

#Chinese Remainder Theorem implemented here.
def CRT(num, exp, p, q, n):
    Vp = pow(num, exp, p)
    Vq = pow(num, exp, q)
    Xp = q * int(BitVector(intVal=q).multiplicative_inverse(BitVector(intVal=p)))
    Xq = p * int(BitVector(intVal=p).multiplicative_inverse(BitVector(intVal=q)))
    return (Vp*Xp + Vq*Xq) % n

def getInput_encrypt(filein):
    inputlist = []
    bv = BitVector( filename=filein )
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file( 128 ) #Get 128 bit data
        while len(bitvec) < 128:
            bitvec += BitVector( textstring=' ' )
        bitvec.pad_from_left(128) #pad zero from left to let the data size be 256 bit
        inputlist.append(int(bitvec))
    return inputlist

def getInput_decrypt(filein):
    inputlist = []
    bv = BitVector( filename=filein )
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file( 256 ) #get the encrypted data by 256 bit
        inputlist.append(int(bitvec))
    return inputlist

#Write the decrypt output 
def getOutput_decrypt(fileout, outputlist):
    fout = open(fileout, 'wb')
    for item in outputlist:
        temp = BitVector(intVal=item, size=256)
        fout.write(temp[128:256].getTextFromBitVector())
    fout.close()

#write the encrypted output
def getOutput_encrypt(fileout, outputlist):
    fout = open(fileout, 'wb')
    for item in outputlist:
        temp = BitVector(intVal=item, size=256)
        fout.write(temp.getTextFromBitVector())
    fout.close()

#encrypt here
def encrypt(inputlist):
    outputlist = []
    while True:
        p = (pg( bits = 128, debug = 0 )).findPrime()
        q = (pg( bits = 128, debug = 0 )).findPrime()
        if BitVector( intVal=p )[0:2] == BitVector( intVal=3 ) and BitVector( intVal=q )[0:2] == BitVector( intVal=3 ) and p != q and gcd(p-1, e) == 1 and gcd(q-1, e) == 1:
            break
    ftemp = open('tempkey.txt', 'w+')
    ftemp.write(str(p) + ' ' + str(q) + '\n')
    ftemp.close()
    n = p * q
    totient = (p - 1) * (q - 1)
    for item in inputlist:
        outputlist.append(CRT(item, e, p, q, n))
    return outputlist

#decrypt here    
def decrypt(inputlist):
    outputlist = []
    ftemp = open('tempkey.txt', 'r')
    temps = ftemp.read()
    ftemp.close()
    p,q = int(temps.split()[0]),int(temps.split()[1])
    n = p * q
    totient = (p - 1) * (q - 1)
    d = int(BitVector(intVal=e).multiplicative_inverse(BitVector(intVal=totient)))
    print d
    for item in inputlist:
        outputlist.append(CRT(item, d, p, q, n))
    return outputlist

def main():
    if sys.argv[1] == '-e':
        inputlist = getInput_encrypt(sys.argv[2])
        outputlist = encrypt(inputlist)
        getOutput_encrypt(sys.argv[3], outputlist)
    if sys.argv[1] == '-d':
        inputlist = getInput_decrypt(sys.argv[2])
        outputlist = decrypt(inputlist)
        getOutput_decrypt(sys.argv[3], outputlist)


if __name__ == "__main__":
    main()
