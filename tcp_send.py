#!/usr/bin/python2

import socket
# calling tcp socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket.socket()
#  if  rec started  listening then we can connect
s.connect(("192.168.10.101",9991))

while  True:
	msg=raw_input("plz enter message : -->>  ")
	s.send(msg)
	print  s.recv(100)


s.close()
