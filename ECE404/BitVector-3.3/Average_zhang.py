#!/usr/local/bin/python

### Created by Zaiwei Zhang

import sys
from BitVector import*


expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

Permutation_Choice1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

Permutation_Choice2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

for z in range(len(Permutation_Choice1)):
    Permutation_Choice1[z] -= 1
for z in range(len(Permutation_Choice2)):
    Permutation_Choice2[z] -= 1


shift_num = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

S1 = [[14,  4,  13,  1,  2,  15,  11,  8,  3, 10,  6,  12,  5,  9,  0,  7],
      [0, 15,   7,  4, 14,   2 , 13,  1, 10,  6, 12,  11,  9,  5,  3,  8], 
      [4,  1,  14,  8, 13,   6 ,  2, 11, 15, 12,  9,   7,  3, 10,  5,  0], 
      [15, 12,   8,  2,  4,   9 ,  1,  7,  5, 11,  3,  14, 10,  0,  6, 13]] 

S2 = [[15,  1,  8,  14,  6,  11,  3,  4,  9,  7,  2,  13,  12,  0,  5,  10], 
      [3, 13,  4,   7, 15,   2,  8, 14, 12,  0,  1,  10,   6,  9, 11,   5], 
      [0, 14,  7,  11, 10,   4, 13,  1,  5,  8, 12,   6,   9,  3,  2,  15], 
      [13,  8, 10,   1,  3,  15,  4,  2, 11,  6,  7,  12,   0,  5, 14,   9]] 

S3 = [[10,  0,  9,  14,  6,  3,  15,  5,  1,  13,  12,  7,  11,  4 , 2,  8], 
      [13,  7,  0,   9,  3,  4,   6, 10,  2,   8,   5, 14,  12, 11, 15,  1], 
      [13,  6,  4,   9,  8, 15,   3,  0, 11,   1,   2, 12,   5, 10, 14,  7], 
      [1, 10, 13,   0,  6,  9,   8,  7,  4,  15,  14,  3,  11,  5,  2, 12]] 

S4 = [[7, 13,  14,  3,  0,  6,  9,  10,  1,  2,  8,  5,  11,  12,  4,  15], 
      [13,  8,  11,  5,  6, 15,  0,   3,  4,  7,  2, 12,   1,  10, 14,   9], 
      [10,  6,   9,  0, 12, 11,  7,  13, 15,  1,  3, 14,   5,   2,  8,   4], 
      [3, 15,   0,  6, 10,  1, 13,   8,  9,  4,  5, 11,  12,   7,  2,  14]] 

S5 = [[2,  12,  4,  1,  7,  10,  11,  6,  8,  5,  3,  15,  13,  0,  14,  9], 
      [14,  11,  2, 12,  4,   7,  13,  1,  5,  0, 15,  10,   3,  9,   8,  6], 
      [4,  2,   1, 11, 10,  13,   7,  8, 15,  9, 12,   5,   6,  3,  0 , 14], 
      [11,  8,  12,  7,  1,  14,   2, 13,  6, 15,  0,   9,  10,  4,  5,   3]] 

S6 = [[12,  1,  10,  15,  9,  2,  6,  8,  0,  13,  3,  4,  14,  7,  5,  11], 
      [10, 15,   4,   2,  7, 12,  9,  5,  6,   1, 13, 14,   0, 11,  3,   8], 
      [9, 14,  15,   5,  2,  8, 12,  3,  7,   0,  4, 10,   1, 13, 11,   6], 
      [4,  3,   2,  12,  9,  5, 15, 10, 11,  14,  1,  7,   6,  0,  8,  13]] 

S7 = [[4, 11,  2,  14,  15,  0,  8,  13,  3,  12,  9,  7,  5,  10,  6,  1], 
      [13,  0, 11,   7,   4,  9,  1,  10, 14,   3,  5, 12,  2,  15,  8,  6], 
      [1,  4, 11,  13,  12,  3,  7,  14, 10,  15,  6 , 8 , 0,   5,  9 , 2], 
      [6, 11, 13,   8,   1,  4, 10,   7,  9,   5,  0, 15, 14,   2,  3, 12]] 

S8 = [[13,  2,  8,  4,  6,  15,  11,  1,  10,  9,  3,  14,  5,  0,  12,  7], 
      [1,  15,  13,  8,  10,  3,  7,  4,  12,  5,  6,  11,  0, 14 ,  9 , 2], 
      [7,  11,   4,  1,   9, 12, 14,  2,   0,  6, 10,  13, 15,  3 ,  5 , 8], 
      [2,   1,  14,  7,   4, 10,  8, 13,  15, 12,  9,   0,  3,  5,   6, 11]] 


sbox = [S1,S2,S3,S4,S5,S6,S7,S8]

pbox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

def helperfunction(inputlist):
    for i in range(len(inputlist)):
        inputlist[i] -= 1

def circular_left_shift(input, num):
    temp = input[0:num]
    input = input.shift_left(num)
    input[(len(input) - num) : (len(input))] = temp
    return input

def get_encryption_key():
    return raw_input("Please Enter the encryption key: ")

def initialize_round_key(input_key):
    key_binary = BitVector(textstring = input_key)
    return key_binary.permute(Permutation_Choice1)
   

def generate_round_key(initial_key):
    round_key_list = []
    for i in range(16):
        initial_key[0:28] = circular_left_shift(initial_key[0:28], shift_num[i])
        initial_key[28:56] = circular_left_shift(initial_key[28:56], shift_num[i])
        #print round_key
        round_key_list.append(initial_key.permute(Permutation_Choice2))
    return round_key_list

def encrypt(filein, fileout, key_list, mode):
    fout = open(fileout, 'w+')
    bv = BitVector( filename = filein )
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file( 64 )
        if len(bitvec) < 64:
            temp_new = BitVector(size = 64)
            temp_new[0:len(bitvec)] = bitvec[0:len(bitvec)]
            temp_new[len(bitvec):64] = BitVector(intVal = 0, size = 64 - len(bitvec))
            bitvec = temp_new
        if len(bitvec) > 0: 
            if mode == 1:
                LE = bitvec[0:32]
                RE = bitvec[32:64]
            else:
                LE = bitvec[32:64]
                RE = bitvec[0:32]
            for i in range(16):
                newRE = RE.permute( expansion_permutation )
                out_xor = newRE ^ key_list[i]
                index1 = 0
                index2 = 0
                sout = BitVector(size = 32)
                for j in range(8):
                    tempx = (out_xor[index1:(index1+6)].permute([0,5,1,2,3,4]))[0:2].intValue()
                    tempy = (out_xor[index1:(index1+6)].permute([0,5,1,2,3,4]))[2:6].intValue()
                    sout[index2:(index2+4)] = BitVector(intVal = sbox[j][tempx][tempy], size = 4)
                    index1 += 6
                    index2 += 4
                pout = sout.permute(pbox)
                finalRE = LE ^ pout
                bitvec[0:32] = RE
                bitvec[32:64] = finalRE
                LE = bitvec[0:32]
                RE = bitvec[32:64]

            if mode == 2:
                bitvec[0:32] = RE
                bitvec[32:64] = LE
        fout.write(bitvec.getTextFromBitVector())
    fout.close()

def compute_Confusion(fileout, filetest):
    sum = 0
    bv1 = BitVector( filename = filetest )
    bv2 = BitVector( filename = fileout )
    while (bv1.more_to_read):
        bitvec1 = bv1.read_bits_from_file( 64 )
        bitvec2 = bv2.read_bits_from_file( 64 )
        for i in range(len(bitvec1)):
            if bitvec1[i] != bitvec2[i]:
                sum += 1
    return sum

def compute_Diffusion(fileout, filein, filetest, num_loop):
    check = 0
    testfileout = open("testfile", "w+")
    bv = BitVector( filename = filein )
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file( 64 )
        if check == num_loop:
            bitvec[0] = bitvec[0] ^ 1
        testfileout.write(bitvec.getTextFromBitVector())
        check += 1
    testfileout.close()
    encrypt("testfile",filetest,keylist,1)
    return compute_Confusion(fileout, filetest)       


helperfunction(Permutation_Choice1)
helperfunction(Permutation_Choice2)
helperfunction(pbox)

key = get_encryption_key()
initial_key = initialize_round_key(key)
keylist = generate_round_key(initial_key)

encrypt(sys.argv[1], sys.argv[2], keylist, 1)

#Five test cases
print "Confusion Test"
#Test Case1
Confusion = 0
testkey1 = BitVector(textstring = key)
testkey1[0] = testkey1[0] ^ 1
print "The key used for testcase1:",testkey1.getTextFromBitVector()
initial_key = testkey1.permute(Permutation_Choice1)
keylist = generate_round_key(initial_key)
encrypt(sys.argv[1], "testfile1", keylist, 1)
Confusion += compute_Confusion(sys.argv[2],"testfile1")

#Test Case2
testkey2 = BitVector(textstring = key)
testkey2[10] = testkey2[10] ^ 1
print "The key used for testcase2:",testkey2.getTextFromBitVector()
initial_key = testkey2.permute(Permutation_Choice1)
keylist = generate_round_key(initial_key)
encrypt(sys.argv[1], "testfile2", keylist, 1)
Confusion += compute_Confusion(sys.argv[2],"testfile2")

#Test Case3
testkey3 = BitVector(textstring = key)
testkey3[30] = testkey3[30] ^ 1
print "The key used for testcase3:",testkey3.getTextFromBitVector()
initial_key = testkey3.permute(Permutation_Choice1)
keylist = generate_round_key(initial_key)
encrypt(sys.argv[1], "testfile3", keylist, 1)
Confusion += compute_Confusion(sys.argv[2],"testfile3")

#Test Case4
testkey4 = BitVector(textstring = key)
testkey4[40] = testkey4[40] ^ 1
print "The key used for testcase4:",testkey4.getTextFromBitVector()
initial_key = testkey4.permute(Permutation_Choice1)
keylist = generate_round_key(initial_key)
encrypt(sys.argv[1], "testfile4", keylist, 1)
Confusion += compute_Confusion(sys.argv[2],"testfile4")

#Test Case2
testkey5 = BitVector(textstring = key)
testkey5[50] = testkey5[50] ^ 1
print "The key used for testcase5:",testkey5.getTextFromBitVector()
initial_key = testkey5.permute(Permutation_Choice1)
keylist = generate_round_key(initial_key)
encrypt(sys.argv[1], "testfile5", keylist, 1)
Confusion += compute_Confusion(sys.argv[2],"testfile5")

print "Confusion Test: The average of the number of ciphertext bits changed for five test cases:",Confusion/5

#Five test cases for Diffusion
initial_key = initialize_round_key(key)
keylist = generate_round_key(initial_key)
print "Diffusion Test"
Diffusion = 0
#Test Case1
print "Diffusion test 1"
Diffusion += compute_Diffusion(sys.argv[2],sys.argv[1],"testfile6", 10)

#Test Case2
print "Diffusion test 2"
Diffusion += compute_Diffusion(sys.argv[2],sys.argv[1],"testfile7", 20)

#Test Case3
print "Diffusion test 3"
Diffusion += compute_Diffusion(sys.argv[2],sys.argv[1],"testfile8", 30)

#Test Case4
print "Diffusion test 4"
Diffusion += compute_Diffusion(sys.argv[2],sys.argv[1],"testfile9", 40)

#Test Case5
print "Diffusion test 5"
Diffusion += compute_Diffusion(sys.argv[2],sys.argv[1],"testfile10", 50)

print "Diffusion Test: The average of the number of ciphertext bits changed for five test cases:",Diffusion/5




