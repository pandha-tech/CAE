import serial
import time
import tkinter as tk
import random
import numpy as np

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


# 워터 펌프
# 워터펌프 켜기
def pump_on() :
    cmd = "g"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 워터펌프 끄기
def pump_off() :
    cmd = "h"
    py_serial.write(cmd.encode())
    time.sleep(0.1)
# 워터펌프 상태 점검
def pump_chk(res) :
    res = int(res)
    if res == 0:
        pump_status = tk.Label(main_disp, text="ON", bg="white", fg="blue")
        pump_status.grid(row=4, column=1)
    elif res == 1:
        pump_status = tk.Label(main_disp, text="OFF", bg="white", fg="red")
        pump_status.grid(row=4, column=1)

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
        pump_stat = int(st_line[24])
        flowrate_stat = str(st_line[26:30])
        #print(v1_stat, v2_stat, flowrate_stat)
        valve_1_chk(v1_stat)
        valve_2_chk(v2_stat)
        pump_chk(pump_stat)
        flow_chk(flowrate_stat)

        if v1_stat == 0 and v2_stat == 0:  # 구간 개방
            interval_chk(0)
        elif v1_stat == 1 and v2_stat == 1:  # 구간 폐쇄
            interval_chk(1)
        elif v1_stat != v2_stat :
            interval_status = tk.Label(main_disp, text="WRONG", bg="red", fg="white")
            interval_status.grid(row=1, column=1)

        main_disp.after(1000, chk_alltime)

# 유량 점검
def flow_chk(flow) :

    flow_stat = tk.StringVar()
    flow_stat.set(flow)
    flow_rate = tk.Label(main_disp, textvariable=flow_stat, bg="white", fg = "blue")
    flow_rate.grid(row=0, column=3)

# 테스트 모드
def test_mode() :

    global adj_flow # 유량 조정값 저장
    global adj_pres # 수압 조정값 저장
    global adj_temp # 온도 조정값 저장

    adj_flow_label = tk.Label(main_disp, text="Flowrate : ")
    adj_flow_label.grid(row=2, column = 2)
    adj_flow_entry = tk.Entry(main_disp)
    adj_flow_entry.grid(row=2, column=3)
    adj_flow = adj_flow_entry.get()

    adj_pres_label = tk.Label(main_disp, text="Pressure : ")
    adj_pres_label.grid(row=3, column=2)
    adj_pres_entry = tk.Entry(main_disp)
    adj_pres_entry.grid(row=3, column=3)
    adj_pres = adj_pres_entry.get()

    adj_temp_label = tk.Label(main_disp, text="Temperature : ")
    adj_temp_label.grid(row=4, column=2)
    adj_temp_entry = tk.Entry(main_disp)
    adj_temp_entry.grid(row=4, column=3)
    adj_temp = adj_temp_entry.get()

    adj_apply = tk.Button(main_disp, text="APPLY", command=test_adj_value)
    adj_apply.grid(row=5, column=2)

def test_adj_value() :
    print("Hello world")




# tkinter GUI 구성
main_disp = tk.Tk()
main_disp.title("CONTROL CONSOLE")
main_disp.geometry("1000x800")
main_disp.resizable(True, True)


pres_stat_list = []
temp_stat_list = []
pres_stat_index = 0
for value in range(1000) :
    pres_stat_list.append(round(random.uniform(15,21.3),2))
    temp_stat_list.append(round(random.uniform(-163,-162),2))

pres_stat_value = tk.StringVar()
temp_stat_value = tk.StringVar()

for pres_stat_index in range(1000):
    pres_stat_value.set(pres_stat_list[pres_stat_index])
    temp_stat_value.set(temp_stat_list[pres_stat_index])

#변수 선언부


#Label, Grid
operation_status_label = tk.Label(main_disp, text="Operation Status :")
operation_status_label.grid(row=0, column=0)

flow_rate_status_label = tk.Label(main_disp, text="Flow rate : ")
flow_rate_status_label.grid(row=0, column=2)

pressure_status_label = tk.Label(main_disp, text="Pressure : ")
pressure_status_label.grid(row=0, column=4)
pres_stat = tk.Label(main_disp, textvariable=pres_stat_value, bg="white", fg="blue")
pres_stat.grid(row=0, column=5)

temp_status_label = tk.Label(main_disp, text="Temperature : ")
temp_status_label.grid(row=0, column=6)
temp_stat = tk.Label(main_disp, textvariable=temp_stat_value, bg="white", fg="blue")
temp_stat.grid(row=0, column=7)

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

pump_on_button = tk.Button(main_disp, text="PUMP ON", command=pump_on)
pump_on_button.grid(row=8, column=0)
pump_off_button = tk.Button(main_disp, text="PUMP OFF", command=pump_off)
pump_off_button.grid(row=8, column=1)

testmode_chk = tk.Checkbutton(main_disp, text = "TEST MODE", command=test_mode)
testmode_chk.grid(row=1, column = 2)

main_disp.after(1000, chk_alltime)


main_disp.mainloop()








