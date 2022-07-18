import serial
import time

py_serial = serial.Serial(port="/dev/cu.usbserial-1140",baudrate = 9600)

while True :

    command = input("킬 릴레이 선택(a,b,c,d) : ")
    py_serial.write(command.encode())

    time.sleep(0.1)

    if py_serial.readable() :

        response = py_serial.readline()
        print(response[:len(response) - 1].decode())



