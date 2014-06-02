from hw05 import *
import wave
cipher = RC4('0123456789ABCDEF')
orig = wave.open('Crypt_laugh.wav','r')
norig = orig.getnframes()
or1 = orig.readframes(norig)
print list(or1)
print len(list(or1))
print norig
#encry = cipher.encrypt(or1)
#decry = cipher.decrypt(encry)
#if or1 == decry:
#    print 'ok'
#else:
#    print 'not ok'
