#! /usr/bin/env python

import socket
from scapy.all import *

class TcpAttack:
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        fout = open("openports.txt", "w+")
        IP = socket.gethostbyname(self.targetIP)
        for port in range(rangeStart, rangeEnd+1):
            #tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #conn = tempsock.connect_ex((IP, port))
            temp = sr(IP(src=self.spoofIP, dst=self.targetIP)/TCP(dport=port))
            print temp
            #if conn == 0:
            #    tmps = "Available port found: "+str(port)+"\n"
            #    fout.write(tmps)
            #    tempsock.close()
            #else:
            #    print "Port "+str(port)+" is closed."
        #fout.close()
    

    def attackTarget(self, port):
        tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = socket.gethostbyname(self.targetIP)
        if tempsock.connect_ex((IP, port)):
            
            return 1
        else:
            return 0
