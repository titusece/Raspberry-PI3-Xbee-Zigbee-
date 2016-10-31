#! /usr/bin/python
import EXbee 

import argparse

parser = argparse.ArgumentParser(description="Get the port")
parser.add_argument("o", type=str, help="Port")
args = parser.parse_args()


#handle = EXbee.EXbee('/dev/ttyUSB0',9600)
handle = EXbee.EXbee(args.o,9600)
handle.API = 1
response = handle.read_rx()	
print response
print "Sender:%s     " % response['SOURCE_ADDRESS_64'] 
print "Message: %s   " % response['DATA']
