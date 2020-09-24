#!/usr/bin/python

import socket
import sys
import time

if len(sys.argv) != 3:

	print "Usage: smtp.py <usernames_list.txt> <host>"
	sys.exit(0)

print "\nEnumerating SMTP users from " + sys.argv[1] + " on host " + sys.argv[2] + '\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((sys.argv[2], 25))

banner = s.recv(1024)


with open(sys.argv[1], "r") as a_file:
        for username in a_file:
		
		s.send('VRFY ' + username + '\r\n')
		
		result = s.recv(1024)
		
		if '252 2.0.0 ' in result:
			print "\033[1;32;40m[+]\033[1;32;0m Valid username: " + "\033[1;32;40m" + username.strip()+ "\033[1;32;0m"
		else:
			print "\033[1;31;40m[-]\033[1;31;0m Invalid username: " + username.strip()

print '\n' + "Done"