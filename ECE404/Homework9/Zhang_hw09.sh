#! /bin/bash
# Homework9: written by Zaiwei Zhang

#flush the previous rules first
iptables -t filter -F

#Then delete the previous chains
iptables -t filter -X

#Create my firewall rules here
#my firewall rules have been implemented in the following
#Place no restriction on outbound packets
iptables -A OUTPUT -j ACCEPT

#Allow for SSH access from only the purdue.edu domain
iptables -A INPUT -s 128.210.7.199 -p tcp --destination-port 22 -j ACCEPT

#Allow a single IP address in the internet to access your machine for the http service
allowed_ip="192.168.0.1"
iptables -A INPUT -s $allowed_ip -p tcp --destination-port 80 -j ACCEPT

#Permit Auth/Ident service that is used by services like SMTP and IRC
iptables -A INPUT -p udp --destination-port 113 -j ACCEPT
iptables -A INPUT -p tcp --destination-port 113 -j ACCEPT

#Accept the ICMP Echo requests coming from the outside
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

#Respond back with TCP RST or ICMP unreadable for incoming requests for blocked ports
iptables -A INPUT -p all -j REJECT --reject-with icmp-host-unreachable


#Output of the iptables after running my script:
Chain INPUT (policy ACCEPT)
target     prot opt source               destination        
ACCEPT     tcp  --  128.210.7.199        anywhere             tcp dpt:ssh
ACCEPT     tcp  --  192.168.0.1          anywhere             tcp dpt:http
ACCEPT     udp  --  anywhere             anywhere             udp dpt:113
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:auth
ACCEPT     icmp --  anywhere             anywhere             icmp echo-request
REJECT     all  --  anywhere             anywhere             reject-with icmp-host-unreachable

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination        

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination        
ACCEPT     all  --  anywhere             anywhere
