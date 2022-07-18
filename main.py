import serial
import time
import tkinter as tk

py_serial = serial.Serial(port="/dev/cu.usbserial-1140",baudrate = 9600)


while True :

    command = input("킬 릴레이 선택(a,b,c,d) : ")
    py_serial.write(command.encode())

    time.sleep(0.1)

    if py_serial.readable() :

        response = py_serial.readline()
        print(response[:len(response) - 1].decode())

main_disp = tk.Tk()
main_disp.geometry("1000x800")
main_disp.resizable(True,True)

valve_1_label = tk.Label(main_disp,text="솔레노이드 밸브 #1 :")
valve_1_label.grid(row=0, column=0)
valve_1_status = tk.Label(main_disp,textvariable = response)
valve_1_status.grid(row=0,column=1)

valve_1_label = tk.Label(main_disp,text="솔레노이드 밸브 #2 :")
valve_1_label.grid(row=1, column=0)
valve_1_status = tk.Label(main_disp,text="정상")
valve_1_status.grid(row=1,column=1)

valve_1_label = tk.Label(main_disp,text="펌프 작동 상태 :")
valve_1_label.grid(row=2, column=0)
valve_1_status = tk.Label(main_disp,text="정상")
valve_1_status.grid(row=2,column=1)

main_disp.mainloop()







