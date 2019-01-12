#!/usr/bin/env python2

import  socket

ip="192.168.10.101"
port=9090   #  port >6000  are generally free to use 

#  calling  UDP  protocol 
#             socket.AF_INET--->ipv4         , socket.SOCK_DGRAM--->  UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# ================================ above this section is common for both sender /receiver

#   rec side only 
#  binding ip and port 
s.bind((ip,port))            # proving  a way to connect 

while  3  >  2	 :

	print   s.recvfrom(100)  
