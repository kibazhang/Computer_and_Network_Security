#! /usr/bin/env python

import time
import socket
#from scapy.all import *

class TcpAttack:
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        fout = open("openports.txt", "w+")
        IP = socket.gethostbyname(self.targetIP)
        #IP_spoof = socket.gethostbyname(self.spoofIP)
        for port in range(rangeStart, rangeEnd+1):
            tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = tempsock.connect_ex((IP, port))
            if conn == 0:
                tmps = "Available port found: "+str(port)+"\n"
                fout.write(tmps)
                tempsock.close()
            else:
                print "Port "+str(port)+" is closed."
        fout.close()

    def attackTarget(self, port):
        tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = socket.gethostbyname(self.targetIP)
        print "Start Dos Attack"
        if tempsock.connect_ex((IP, port)):
            tempsock.send('Attacking')
            time.sleep(1)
            return 1
        else:
            return 0
