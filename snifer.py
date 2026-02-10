import serial

ser = serial.Serial(port='COM1', baudrate=9600, timeout=1)
ser.write(b'command')
data = ser.readline()
ser.close()