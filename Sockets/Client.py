#!/usr/bin/env python
 
import socket
 
s = socket.socket()
 
s.connect(("10.219.1.219", 5555))
 
while True:
    mensaje = raw_input("Write a command: ")
 
    s.send(mensaje)
 
    if mensaje == "close":
        break
 
print "The connection was closed"
 
s.close()
