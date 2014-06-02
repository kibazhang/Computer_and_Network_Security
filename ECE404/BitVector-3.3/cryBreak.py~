#!/usr/bin/env python

###  BruteForceAttack.py
###  Avi Kak  (kak@purdue.edu)
###  January 22, 2014
    
import os, sys

keys = [chr(i) + chr(j) for i in range(65,123) for j in range(65,123)]
for key in keys:
    print "key is: ", key
    arg = 'echo ' +  key + r' | DecryptForFun.py output5.txt recover5.txt 2>&1 1>/dev/null'
    os.system(arg)
    match = os.system("grep -i 'mark twain' recover5.txt > junk.txt")
    try:
        size = os.path.getsize("junk.txt")
    except: pass
    if size > 0:
        sys.exit(0) 
