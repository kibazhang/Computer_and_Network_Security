import hashlib
import sys

temp = hashlib.sha512()
fin = open(sys.argv[1], 'r')
temps = fin.read()
temp.update(temps)
print temp.hexdigest()
