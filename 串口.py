# -*- coding: utf-8 -*
import serial
import time
import binascii

ser = serial.Serial("/dev/ttyAMA0",256000)

if not ser.isOpen():
    print("open failed")
else:
    print("open success: ")
    print(ser)

try:
    while True:
        count = ser.inWaiting()
        if count > 0:
            recv = ser.read(count)
            hex_str = binascii.hexlify(recv).decode()
            hex_array = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)] #十进制
            #hex_array = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)] #十六进制
            print(hex_array)
            ser.write(hex_array) #十进制
            #ser.write(binascii.unhexlify(''.join(hex_array)))  #十六进制
        time.sleep(0.05) 
except KeyboardInterrupt:
    if ser != None:
        ser.close()
