#! /usr/bin/python
import EXbee 
import argparse

parser = argparse.ArgumentParser(description="Get the payload and MAC ID of Xbee Receiver")
parser.add_argument("i", type=str, help="MAC ID")
parser.add_argument("p", type=str, help="Payload")
parser.add_argument("o", type=str, help="Port")
args = parser.parse_args()


#handle = EXbee.EXbee('/dev/ttyUSB0',9600)
handle = EXbee.EXbee(args.o,9600)
handle.API = 1
#response = handle.send_tx("Glory to GOD, JESUS & HOLYSPIRIT!!!","0013A20040E793E8","02")

response = handle.send_tx(args.p,args.i,"02")
print response
if response['Delivery_status'][:2] == "00":
	print "Frame sent with success"
else:
	print "Failed"	
