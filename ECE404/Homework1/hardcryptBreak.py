The following script runs a brute-force attack on the encrypted text:
20352a7e36703a6930767f7276397e376528632d6b6665656f6f6424623c2d30272f3c2d3d2172396933742c7e233f687d2e32083c11385a03460d440c25

By running the following command:
python cryptBreak.py output5.txt out

I get the decrypted output:
The secret of getting ahead is getting started. -- Mark Twain

The encrypted key is: ok.
Binary key version: 0110111101101011.

My algorithm runs a brute-force attack from input bits: 0000000000000000 to 1111111111111111. Therefore, it takes sometime to finish the brute-force attack.

#!/usr/bin/env python

PassPhrase = "Hopes and dreams of a million years"

import sys
from BitVector import *                                         #(A)

if len(sys.argv) is not 3:                                      #(B)
    sys.exit('''Needs two command-line arguments, one for '''
             '''the encrypted file and the other for the '''
             '''decrypted output file''')

BLOCKSIZE = 16                                                  #(C)
numbytes = BLOCKSIZE / 8                                        #(D)

# Reduce the passphrase to a bit array of size BLOCKSIZE:
bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)                      #(E)
for i in range(0,len(PassPhrase) / numbytes):                   #(F)
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes]             #(G)
    bv_iv ^= BitVector( textstring = textstr )                  #(H)

# Create a bitvector from the ciphertext hex string:
FILEIN = open(sys.argv[1])                                      #(I)
encrypted_bv = BitVector( hexstring = FILEIN.read() )           #(J)

check = 1
#Create the input testing and make a brute attack
for temp1 in range(2**8):
    key1 = ""
    for j in range(8):
        key1 += str(temp1 % 2)
        temp1 = int(temp1 / 2)
    temp_key1 = chr(int(key1,2))
    for temp2 in range(2**8):
        key2 = ""
        for h in range(8):
            key2 += str(temp2 % 2)
            temp2 = int(temp2 / 2)
        temp_key2 = chr(int(key2,2))
        key = temp_key1 + temp_key2
  
        # Reduce the key to a bit array of size BLOCKSIZE:
        key_bv = BitVector(bitlist = [0]*BLOCKSIZE)                     #(P)
        for i in range(0,len(key) / numbytes):                          #(Q)
            keyblock = key[i*numbytes:(i+1)*numbytes]                   #(R)
            key_bv ^= BitVector( textstring = keyblock )                #(S)

        print "Testing binary key =", key_bv
        # Create a bitvector for storing the output plaintext bit array:
        msg_decrypted_bv = BitVector( size = 0 )                        #(T)

        # Carry out differential XORing of bit blocks and decryption:
        previous_decrypted_block = bv_iv                                #(U)
        for i in range(0, len(encrypted_bv) / BLOCKSIZE):               #(V)
            bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]              #(W)
            temp = bv.deep_copy()                                       #(X)
            bv ^=  previous_decrypted_block                             #(Y)
            previous_decrypted_block = temp                             #(Z)
            bv ^=  key_bv                                               #(a)
            msg_decrypted_bv += bv                                      #(b)

        outputtext = msg_decrypted_bv.getTextFromBitVector()            #(c)
        temp_out = outputtext.split()
        for item in temp_out:
            if item == "The":
                check = 0
                break
        if check == 0:
            break
    if check == 0:
        break

print "Binary key =", key1+key2
print "ASCII key =", key
# Write the plaintext to the output file:
FILEOUT = open(sys.argv[2], 'w')                                #(d)
FILEOUT.write(outputtext)                                       #(e)
FILEOUT.close()                                                 #(f)
