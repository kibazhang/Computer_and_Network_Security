#! /usr/bin/env python

import socket
#import scapy

class TcpAttack:
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        fout = open("openports.txt", "w+")
        for i in range(rangeStart, rangeEnd+1):
            tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                tempsock.connect((self.targetIP, i))
                tmps = "Available port found: "+str(i)+"\n"
                fout.write(tmps)
                tempsock.close()
            except socket.error as msg:
                print msg
                print "Port "+str(i)+" is closed."
        fout.close()
