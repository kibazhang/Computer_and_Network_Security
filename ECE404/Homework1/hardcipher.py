The following script is used to implement the Vigenere polyalphabetic cipher. The input will be a standard text file, and as well as the output will be.

import sys

#Checking for the input
if len(sys.argv) is not 3:                
    sys.exit('''Needs two command-line arguments, one for '''
             '''the encrypted file and the other for the '''
             '''decrypted output file''')

#Get the input from the input file
FILEIN = open(sys.argv[1])
plaintext = FILEIN.read()

#Get the key from user
key = raw_input("Please enter the encryption key: ")
outputtext = ""

#Encrypting Here
for i in range(len(plaintext)):
    if plaintext[i] == plaintext[i].lower():
        if key[i%len(key)] == key[i%len(key)].lower():
            outputtext += chr(ord(key[i%len(key)]) - 97 + ord(plaintext[i])).upper()
        else:
            outputtext += chr(ord(key[i%len(key)]) - 65 + ord(plaintext[i])).upper()

    elif plaintext[i] == plaintext[i].upper():
        if key[i%len(key)] == key[i%len(key)].lower():
            outputtext += chr(ord(key[i%len(key)]) - 97 + ord(plaintext[i])).lower()
        else:
            outputtext += chr(ord(key[i%len(key)]) - 65 + ord(plaintext[i])).lower()
        
# Write the plaintext to the output file:
FILEOUT = open(sys.argv[2], 'w')
FILEOUT.write(outputtext)
FILEOUT.close()          

The following are some examples:
plaintext:  Meetmeatnight
encryption key: AB
ciphertext: mFEUMFAUNJGIT

To distinguish lowercase and uppercase, if the input plaintext is lowercase, the ciphertext will be uppercase. The encrytion key will be treated separately for lowercase and uppercase. For example, if the encryption key is 'A', the position added will be 'A' - 65. If the encryption key is 'a', the position added will be 'a' - 97.

Another example:
plaintext:  IHaveTheGood
encryption key:Ac
ciphertext: ijAXEvHGgQOF

Another example:
plaintext:  iAMtheMAN
encryption key:Bb
ciphertext: JbnUIFnbo













