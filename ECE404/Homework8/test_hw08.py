#! /usr/bin/env python

from zhang_hw08 import *
spoofIP = '10.185.37.87'
targetIP = 'ecelinux46.ecn.purdue.edu'
rangeStart = 0
rangeEnd = 5000
Tcp = TcpAttack('spoofIP', 'targetIP')
Tcp.scanTarget(rangeStart, rangeEnd)
