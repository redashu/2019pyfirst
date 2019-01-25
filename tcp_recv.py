#!/usr/bin/python2

import socket
# calling tcp socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket.socket()
# binding  ip and port 
s.bind(("",9991))
#  listen  number of consecutive connection 
s.listen(50)  #  max  50  connections 
#  re must accept connection from  client 
#  data variable --??client ip+port , client socket 
while  True:
	cliskt,cliaddr=s.accept()
	print  cliskt
	print  cliaddr
	print  cliskt.recv(100)
	cliskt.send("ok",cliaddr)

s.close()
