#!/usr/bin/python


# * PiHome v1.0
# * http://pihome.harkemedia.de/
# *
# * PiHome Copyright 2012, Sebastian Harke
# * Lizenz Informationen.
# * 
# * This work is licensed under the Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Unported License. To view a copy of this license,
# * visit: http://creativecommons.org/licenses/by-nc-sa/3.0/. 


import cgi,time,string,serial,datetime,commands
from os import curdir, sep, path
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


### Serial Port Settings ###
port = '/dev/tty.usbmodem411'
baut_rate = 9600
arduino = serial.Serial(port, baut_rate)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if str(self.path).count(".") != 0:
	            if str(self.path).split(".")[1] == "html":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'text/html')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif str(self.path).split(".")[1] == "css":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'text/html')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif str(self.path).split(".")[1] == "js":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'text/html')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif str(self.path).split(".")[1] == "png":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'image/png')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif str(self.path).split(".")[1] == "gif":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'image/gif')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif self.path.split(".")[1] == "jpg":
	                d = open(curdir + sep + self.path)
	                self.send_response(200)
	                self.send_header('Content-type', 'image/jpeg')
	                self.end_headers()
	                self.wfile.write(d.read())
	                d.close()
	                return
	                
	            elif str(self.path).split("/")[1].split(".")[0] == "request":
	            	self.send_response(200)
	                self.send_header('Content-type', 'text/html')
	                self.end_headers()                
	                datastring = str(self.path).split("?s=")[1]                
	                schalter = datastring.split("/")[0]	                
	                blockA = datastring.split("/")[0]
	                stustfile = blockA + ".txt"
	                signal = datastring.split("/")[1]
	                
	                # Schalter A
	                if schalter == "A":
	                	if signal == "on":
	                		self.wfile.write("1")
	                		# set pin 1 HIGH 
	                		commands.getoutput('echo 1 > status/' + stustfile)
	                		arduino.write("A")
	                	elif signal == "off":
	                		self.wfile.write("0")
	                		# set pin 1 LOW 
	                		commands.getoutput('echo 0 > status/' + stustfile)
	                		arduino.write("B")
	                	elif signal == "status":
	                		if path.exists('status/' + stustfile):
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                		else:
	                			commands.getoutput('echo 0 > status/' + stustfile)
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                
	                # Schalter B		
	                if schalter == "B":
	                	if signal == "on":
	                		self.wfile.write("1")
	                		# set pin 2 HIGH
	                		commands.getoutput('echo 1 > status/' + stustfile) 
	                		arduino.write("C")
	                	elif signal == "off":
	                		self.wfile.write("0")
	                		# set pin 2 LOW
	                		commands.getoutput('echo 0 > status/' + stustfile)
	                		arduino.write("D")
	                	elif signal == "status":
	                		if path.exists('status/' + stustfile):
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                		else:
	                			commands.getoutput('echo 0 > status/' + stustfile)
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                
	                # Schalter C		
	                if schalter == "C":
	                	if signal == "on":
	                		self.wfile.write("1")
	                		# set pin 3 HIGH 
	                		commands.getoutput('echo 1 > status/' + stustfile)
	                		arduino.write("E")
	                	elif signal == "off":
	                		self.wfile.write("0")
	                		# set pin 3 LOW 
	                		commands.getoutput('echo 0 > status/' + stustfile)
	                		arduino.write("F")
	                	elif signal == "status":
	                		if path.exists('status/' + stustfile):
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                		else:
	                			commands.getoutput('echo 0 > status/' + stustfile)
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                
	                # Schalter D		
	                if schalter == "D":
	                	if signal == "on":
	                		self.wfile.write("1")
	                		# set pin 4 HIGH
	                		commands.getoutput('echo 1 > status/' + stustfile)
	                		arduino.write("G")
	                	elif signal == "off":
	                		self.wfile.write("0")
	                		# set pin 4 LOW 
	                		commands.getoutput('echo 0 > status/' + stustfile)
	                		arduino.write("H")
	                	elif signal == "status":
	                		if path.exists('status/' + stustfile):
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                		else:
	                			commands.getoutput('echo 0 > status/' + stustfile)
	                			self.wfile.write(commands.getoutput('cat status/' + stustfile))
	                		
	                return
            else: 
            	# Default Index.html Page
            	d = open(curdir + sep + "/index.html")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(d.read())
                d.close()
                return         
                
            return            
        except IOError:
        	# 404 Error
            self.send_error(404,'File Not Found: ' + self.path)    




def main():
    try:
        srv = HTTPServer(('', 80), Handler)
        print 'START HomeCtrl SERVER'
        srv.serve_forever()
    except KeyboardInterrupt:
        print ' STOP HomeCtrl SERVER'
        srv.socket.close()


main()

