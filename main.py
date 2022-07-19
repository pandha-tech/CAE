import serial
import time
import tkinter as tk

py_serial = serial.Serial(port="/dev/cu.usbserial-1140",baudrate = 9600) # 아두이노 시리얼 포트정보 입력

# 솔레노이드 밸브 #1 켜기(열기)
def valve_1_open() :
    cmd = "a"
    py_serial.write(cmd.encode())
    time.sleep(1)
    res = py_serial.readline()
    res = res[:len(res)-1].decode()
    valve_1_chk(res)

# 솔레노이드 밸브 #1 끄기(닫기)
def valve_1_close() :
    cmd = "b"
    py_serial.write(cmd.encode())
    time.sleep(1)
    res = py_serial.readline()
    res = res[:len(res) - 1].decode()
    valve_1_chk(res)

# 솔레노이드 밸브 #1 상태 점검
def valve_1_chk(res) :
    res = int(res)
    if res == 0 :
        valve_1_status = tk.Label(main_disp,text="OPENED", fg="blue", bg="white")
        valve_1_status.grid(row=2, column=1)
    elif res == 1 :
        valve_1_status = tk.Label(main_disp, text="CLOSED", fg="red", bg="white")
        valve_1_status.grid(row=2, column=1)

# 솔레노이드 밸브 #2 켜기(열기)
def valve_2_open() :
    cmd = "c"
    py_serial.write(cmd.encode())
    time.sleep(1)
    res = py_serial.readline()
    res = res[:len(res)-1].decode()
    valve_2_chk(res)

# 솔레노이드 밸브 #2 끄기(닫기)
def valve_2_close() :
    cmd = "d"
    py_serial.write(cmd.encode())
    time.sleep(1)
    res = py_serial.readline()
    res = res[:len(res) - 1].decode()
    valve_2_chk(res)

# 솔레노이드 밸브 #2 상태 점검
def valve_2_chk(res) :

    res = int(res)
    if res == 0 :
        valve_2_status = tk.Label(main_disp,text="OPENED", fg="blue", bg="white")
        valve_2_status.grid(row=3, column=1)
    elif res == 1 :
        valve_2_status = tk.Label(main_disp, text="CLOSED", fg="red", bg="white")
        valve_2_status.grid(row=3, column=1)

# tkinter GUI 구성
main_disp = tk.Tk()
main_disp.title("CONTROL CONSOLE")
main_disp.geometry("1000x800")
main_disp.resizable(True, True)

#변수 선언부


#Label, Grid
operation_status_label = tk.Label(main_disp, text="Operation Status :")
operation_status_label.grid(row=0, column=0, columnspan=3)

flow_rate_status_label = tk.Label(main_disp, text="Flow rate : ")
flow_rate_status_label.grid(row=0, column=4, columnspan=3)
flow_rate = tk.Label(main_disp, text="25.3 L/M", bg="white", fg="blue")
flow_rate.grid(row=0, column=8)

pressure_status_label = tk.Label(main_disp, text="Pressure : ")
pressure_status_label.grid(row=0, column=9)

temp_status_label = tk.Label(main_disp, text="Temperature : ")
temp_status_label.grid(row=0, column=10)

interval_label = tk.Label(main_disp, text="Interval #1 Status : ")
interval_label.grid(row=1, column=0)
interval_status = tk.Label(main_disp, text="NORMAL", bg="white", fg="blue")
interval_status.grid(row=1, column=1)

#솔레노이드 밸브 #1 : 릴레이 CH2
valve_1_label = tk.Label(main_disp, text="Valve #1 Status :")
valve_1_label.grid(row=2, column=0)

#솔레노이드 밸브 #2 : 릴레이 CH3
valve_2_label = tk.Label(main_disp, text="Valve #2 Status :")
valve_2_label.grid(row=3, column=0)

#펌프 : 릴레이 CH4
pump_label = tk.Label(main_disp, text="Pump Status :")
pump_label.grid(row=4, column=0)
pump_status = tk.Label(main_disp, text="NORMAL", bg="white", fg="blue")
pump_status.grid(row=4, column=1)

interval_open = tk.Button(main_disp, text="INTERVAL #1 OPEN")
interval_open.grid(row=5, column=0)
interval_close = tk.Button(main_disp, text="INTERVAL #1 CLOSE")
interval_close.grid(row=5, column=1)

valve_1_on_button = tk.Button(main_disp, text="Valve #1 OPEN", command=valve_1_open)
valve_1_on_button.grid(row=6, column=0)
valve_1_off_button = tk.Button(main_disp, text="Valve #1 CLOSE", command=valve_1_close)
valve_1_off_button.grid(row=7, column=0)

valve_2_on_button = tk.Button(main_disp, text="Valve #2 OPEN", command=valve_2_open)
valve_2_on_button.grid(row=6, column=1)
valve_2_off_button = tk.Button(main_disp, text="Valve #2 CLOSE", command=valve_2_close)
valve_2_off_button.grid(row=7, column=1)

main_disp.mainloop()








