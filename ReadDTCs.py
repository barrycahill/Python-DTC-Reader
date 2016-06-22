import serial
# import pyserial

device_name = '/dev/tty.OBDII-SPPDev'
ser = serial.Serial('device_name', 38400, timeout=1)
# Connect to the bluetooth OBD-II connector

ser.write("03 \r")
# This requests 'mode 3' which is all stored DTCs
# DTCs should be returned in 3 codes per message frame
# info to decode is here : https://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_3_.28no_PID_required.29

while:
    DTC = ser.readline().split(' ')
    print 'Serial output is: ', DTC
