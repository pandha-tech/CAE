import serial
import time
import tkinter as tk

'''
py_serial = serial.Serial(port="/dev/cu.usbserial-1140",baudrate = 9600)

while True :

    command = input("킬 릴레이 선택(a,b,c,d) : ")
    py_serial.write(command.encode())

    time.sleep(0.1)

    if py_serial.readable() :

        response = py_serial.readline()
        print(response[:len(response) - 1].decode())
'''

main_disp = tk.Tk()
main_disp.title("CONTROL CONSOLE")
main_disp.geometry("1000x800")
main_disp.resizable(True,True)

operation_status_label = tk.Label(main_disp,text="Operation Status :")
operation_status_label.grid(row=0, column=0, columnspan=3)

flow_rate_status_label = tk.Label(main_disp, text="Flow rate : ")
flow_rate_status_label.grid(row=0, column=4, columnspan=3)
flow_rate = tk.Label(main_disp, text="25.3 L/M", bg="white", fg="blue")
flow_rate.grid(row=0, column=8)

pressure_status_label = tk.Label(main_disp, text="Pressure : ")
pressure_status_label.grid(row=0, column=9)

temp_status_label = tk.Label(main_disp, text="Temperature : ")
temp_status_label.grid(row=0, column=10)

interval_label = tk.Label(main_disp,text="Interval #1 Status : ")
interval_label.grid(row=1, column=0)
interval_status = tk.Label(main_disp,text="NORMAL", bg="white", fg="blue")
interval_status.grid(row=1, column=1)


valve_1_label = tk.Label(main_disp,text="Valve #1 Status :")
valve_1_label.grid(row=2, column=0)
valve_1_status = tk.Label(main_disp,text="NORMAL", bg="white", fg="blue")
valve_1_status.grid(row=2,column=1)

valve_2_label = tk.Label(main_disp,text="Valve #2 Status :")
valve_2_label.grid(row=3, column=0)
valve_2_status = tk.Label(main_disp,text="NORMAL", bg="white", fg="blue")
valve_2_status.grid(row=3,column=1)

pump_label = tk.Label(main_disp,text="Pump Status :")
pump_label.grid(row=4, column=0)
pump_status = tk.Label(main_disp,text="NORMAL", bg="white", fg="blue")
pump_status.grid(row=4,column=1)

interval_open = tk.Button(main_disp, text="INTERVAL #1 OPEN")
interval_open.grid(row=5, column=0)
interval_close = tk.Button(main_disp, text="INTERVAL #1 CLOSE")
interval_close.grid(row=5, column=1)

valve_1_on_button = tk.Button(main_disp,text="Valve #1 ON")
valve_1_on_button.grid(row=6, column=0)
valve_1_off_button = tk.Button(main_disp,text="Valve #1 OFF")
valve_1_off_button.grid(row=7, column=0)

valve_2_on_button = tk.Button(main_disp,text="Valve #2 ON")
valve_2_on_button.grid(row=6, column=1)
valve_2_off_button = tk.Button(main_disp,text="Valve #2 OFF")
valve_2_off_button.grid(row=7, column=1)

main_disp.mainloop()







