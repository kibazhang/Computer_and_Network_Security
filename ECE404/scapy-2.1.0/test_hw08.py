#! /usr/bin/env python

from zhang_hw08 import *
spoofIP = 'ecelinux11.ecn.purdue.edu'
targetIP = 'ecelinux46.ecn.purdue.edu'
rangeStart = 0
rangeEnd = 25
Tcp = TcpAttack(spoofIP, targetIP)
Tcp.scanTarget(rangeStart, rangeEnd)
