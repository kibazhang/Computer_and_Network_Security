import wave
import copy
from BitVector import*

class RC4:
    def __init__(self, key):
        #initialize the state vector
        state_vec = [i for i in range(256)]
        tempkey = BitVector( textstring = key )
        i = 0
        k_vec = []
        #permute the key vector
        while i < len(tempkey):
            temp = BitVector( bitstring=str(tempkey[i:(i+8)]) )
            k_vec.append(int(temp))
            i += 8
        T_vec = []
        #get the temp vector
        for i in range(256):
            T_vec.append(k_vec[i%len(k_vec)])
        j = 0
        #get the permuted state vector
        for i in range(256):
            j = (j + state_vec[i] + T_vec[i]) % 256
            state_vec[i],state_vec[j] = state_vec[j],state_vec[i]
        self.s = state_vec
        #print self.s
    def encrypt(self, audio):
        #deep copy in case change the sequence
        temps = copy.deepcopy(self.s)
        temp = list(audio)
        i, j = 0, 0
        output = ''
        #do the encrypt here
        for n in range(len(temp)):
            i = (i + 1) % 256
            j = (j + (temps)[i]) % 256
            temps[i],temps[j] = temps[j],temps[i]
            k = (temps[i] + temps[j]) % 256
            #get the output sequence
            output += (((BitVector(textstring = temp[n])))^BitVector(intVal = temps[k], size = 8)).getTextFromBitVector()
        return output
    def decrypt(self, audio):
        #same logic for decryption
        #use the same state vector
        temps = copy.deepcopy(self.s)
        temp = list(audio)
        i, j = 0, 0
        output = ''
        for n in range(len(temp)):
            i = (i + 1) % 256
            j = (j + (temps)[i]) % 256
            temps[i],temps[j] = temps[j],temps[i]
            k = (temps[i] + temps[j]) % 256
            output += (((BitVector(textstring = temp[n])))^(BitVector(intVal = temps[k], size = 8))).getTextFromBitVector()
        return output
        
            
