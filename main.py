import serial
import time
import tkinter as tk

py_serial = serial.Serial(port="/dev/cu.usbserial-1140",baudrate = 9600) # 아두이노 시리얼 포트정보 입력
condition = True

# 솔레노이드 밸브 #1
# 솔레노이드 밸브 #1 켜기(열기)
def valve_1_open() :
    cmd = "a"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 솔레노이드 밸브 #1 끄기(닫기)
def valve_1_close() :
    cmd = "b"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 솔레노이드 밸브 #1 상태 점검
def valve_1_chk(res) :
    res = int(res)
    if res == 0 :
        valve_1_status = tk.Label(main_disp,text="OPENED", fg="blue", bg="white")
        valve_1_status.grid(row=2, column=1)
    elif res == 1 :
        valve_1_status = tk.Label(main_disp, text="CLOSED", fg="red", bg="white")
        valve_1_status.grid(row=2, column=1)


# 솔레노이드 밸브 #2
# 솔레노이드 밸브 #2 켜기(열기)
def valve_2_open() :
    cmd = "c"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 솔레노이드 밸브 #2 끄기(닫기)
def valve_2_close() :
    cmd = "d"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 솔레노이드 밸브 #2 상태 점검
def valve_2_chk(res) :
    res = int(res)
    if res == 0 :
        valve_2_status = tk.Label(main_disp,text="OPENED", fg="blue", bg="white")
        valve_2_status.grid(row=3, column=1)
    elif res == 1 :
        valve_2_status = tk.Label(main_disp, text="CLOSED", fg="red", bg="white")
        valve_2_status.grid(row=3, column=1)


# 구간 동시 작동
# 구간 열림
def interval_open() :
    cmd = "e"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 구간 닫힘
def interval_close() :
    cmd = "f"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 구간 상태 점검
def interval_chk(res) :
    res = int(res)
    if res == 0 :
        interval_status = tk.Label(main_disp, text="NORMAL", bg="white", fg="green")
        interval_status.grid(row=1, column=1)
    elif res == 1 :
        interval_status = tk.Label(main_disp, text="CLOSED", bg="white", fg="red")
        interval_status.grid(row=1, column=1)

# 상태 항시 점검
def chk_alltime() :

    if condition :
        st_line = py_serial.readline()
        st_line = st_line[:len(st_line) - 1].decode()
        v1_stat = int(st_line[8])
        v2_stat = int(st_line[17])
        print(v1_stat, v2_stat)
        valve_1_chk(v1_stat)
        valve_2_chk(v2_stat)

        if v1_stat == 0 and v2_stat == 0:  # 구간 개방
            interval_chk(0)
        elif v1_stat == 1 and v2_stat == 1:  # 구간 폐쇄
            interval_chk(1)
        elif v1_stat != v2_stat :
            interval_status = tk.Label(main_disp, text="WRONG", bg="red", fg="white")
            interval_status.grid(row=1, column=1)

        main_disp.after(100, chk_alltime)


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

interval_open = tk.Button(main_disp, text="INTERVAL #1 OPEN", command=interval_open)
interval_open.grid(row=5, column=0)
interval_close = tk.Button(main_disp, text="INTERVAL #1 CLOSE", command=interval_close)
interval_close.grid(row=5, column=1)

valve_1_on_button = tk.Button(main_disp, text="Valve #1 OPEN", command=valve_1_open)
valve_1_on_button.grid(row=6, column=0)
valve_1_off_button = tk.Button(main_disp, text="Valve #1 CLOSE", command=valve_1_close)
valve_1_off_button.grid(row=7, column=0)

valve_2_on_button = tk.Button(main_disp, text="Valve #2 OPEN", command=valve_2_open)
valve_2_on_button.grid(row=6, column=1)
valve_2_off_button = tk.Button(main_disp, text="Valve #2 CLOSE", command=valve_2_close)
valve_2_off_button.grid(row=7, column=1)

main_disp.after(100, chk_alltime)

main_disp.mainloop()








