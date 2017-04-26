#!/usr/bin/python
import time
from subprocess import call
import socket
import time
import wiringpi2 as gpio
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

#Define the Ultrasonic Sensor Pins in use
Trig = 11
Echo = 13

#Create Socket (FAMILY,TYPE)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create the socket with the address and port
server.bind(("",5555))

#Listening for incoming connections
server.listen(1)

print "Setting GPIO"
gpio.wiringPiSetupGpio()

#Establish use of pins
GPIO.setup(Trig, GPIO.OUT) #pin of HC-SR04
GPIO.setup(Echo, GPIO.IN) #pin of HC-SR04

gpio.pinMode(17,1) #LPOWER PWM
gpio.pinMode(18,1) #RPOWER PWM

gpio.pinMode(22,1) #DIR
gpio.pinMode(23,1) #DIR


gpio.softPwmCreate(17,0,100)
gpio.softPwmCreate(18,0,100)
print "GPIO Ok"

print"Waiting for connection"
connection, clientAddress = server.accept()

def saveInFile(right, left, InFront, back):
	#Open File and Save info
	fo = open("info.txt", "wb")
	strWrite = "RIGHT: " + str(right)+ "\n" + "LEFT: " + str(left) +"\n" +"FRONT: " + str(InFront) +"\n" + "BACK: " +str(back)
	fo.write(strWrite)
	

def getDistance():   
	   GPIO.output(Trig, False) 
	   time.sleep(2*10**-6)
	   GPIO.output(Trig, True) 
	   time.sleep(10*10**-6)
	   GPIO.output(Trig, False) 
	 
	  #Start time when Echo is High
	   start = 0
	   end = 0
	   
	   while GPIO.input(Echo) == 0:
	      start = time.time()
	      print start	
	      print "START"
	 
	   while GPIO.input(Echo) == 1:
	      end = time.time()	
	      print end
	      print "END"
	 
	   duracion = end-start		   
	   duracion = duracion*10**-6	   
	   medida = duracion/58 
	    
	   print "MEDIDA"	
	   print medida
	   return medida
		
def right():
	l_power = 0
	r_power = 150 
	gpio.softPwmWrite(5,r_power)
        gpio.softPwmWrite(18,l_power)


def backward():  
	gpio.digitalWrite(22,1)
	gpio.digitalWrite(23,0)
	gpio.softPwmWrite(18,250)
	gpio.softPwmWrite(5,250)
	print "back"

def turnLeft():
	forward()
	time.sleep(10*10**-6)
	right()

def forward(): 
	gpio.digitalWrite(22,0)
	gpio.digitalWrite(23,1)
	gpio.softPwmWrite(18,250)
	gpio.softPwmWrite(5,250)	
	print "go"


def turnRight():
	backward()
	time.sleep(10*10**-6)
	right()


def stop(): 
	gpio.digitalWrite(22,0)
	gpio.digitalWrite(23,0)
	gpio.softPwmWrite(5,0)
	gpio.softPwmWrite(18,0)
	print "stop"

def read(): 
	inFront = getDistance()
	turnRight()
	time.sleep(2*10**-6)
	stop()
	right = getDistance()
	turnRight()
	time.sleep(2*10**-6)
	stop()
	back = getDistance()
	turnRight()
	time.sleep(2*10**-6)
	stop()
	left = getDistance()
	turnRight()
	time.sleep(2*10**-6)
	stop()
	saveInFile(right, left, inFront, back)
		
	

def close(): 
	connection.close()
	server.close()


while True:
	data = connection.recv(1024)
	
	if data == "back":
		backward()
	
	if data =="go":
		forward()

	if data == "stop":
		stop()

	if data == "right":
		turnRight()
		
	if data == "left":
		turnLeft()

	if data == "read":
		read()
		
	if data == "close":
		close()
		
	
	















