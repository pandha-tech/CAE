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

    global flow_stat
    flow_stat = tk.StringVar()
    flow_stat.set(flow)
    flow_rate = tk.Label(main_disp, textvariable=flow_stat, bg="white", fg = "blue")
    flow_rate.grid(row=0, column=1)

# 테스트 모드
def test_mode() :

    global adj_flow
    global adj_pres
    global adj_temp

    adj_flow = tk.DoubleVar()
    adj_pres = tk.DoubleVar()
    adj_temp = tk.DoubleVar()

    adj_flow_label = tk.Label(main_disp, text="Flowrate : ")
    adj_flow_label.grid(row=2, column = 2)
    adj_flow_entry = tk.Entry(main_disp, textvariable=adj_flow)
    adj_flow_entry.grid(row=2, column=3)
    adjusted_flow_label = tk.Label(main_disp, text="Adjusted : ")
    adjusted_flow_label.grid(row=2, column=4)

    adj_pres_label = tk.Label(main_disp, text="Pressure : ")
    adj_pres_label.grid(row=3, column=2)
    adj_pres_entry = tk.Entry(main_disp, textvariable=adj_pres)
    adj_pres_entry.grid(row=3, column=3)
    adjusted_pres_label = tk.Label(main_disp, text="Adjusted : ")
    adjusted_pres_label.grid(row=3, column=4)

    adj_temp_label = tk.Label(main_disp, text="Temperature : ")
    adj_temp_label.grid(row=4, column=2)
    adj_temp_entry = tk.Entry(main_disp, textvariable=adj_temp)
    adj_temp_entry.grid(row=4, column=3)
    adjusted_temp_label = tk.Label(main_disp, text="Adjusted : ")
    adjusted_temp_label.grid(row=4, column=4)

    adj_apply = tk.Button(main_disp, text="APPLY", command=test_adj_value)
    adj_apply.grid(row=5, column=2)

def test_adj_value() :

    # 정상범위 조건
    # 유량 : 10 ~ 30 L/Min
    # 압력 : 0 ~ 21.3 MPa
    # 온도 : -164 ~ -161 degree of C

    # 3개 중 하나라도 이상치가 나오면 차단
    if float(adj_flow.get()) < 10 or float(adj_flow.get()) > 30 or float(adj_pres.get()) < 0 or float(adj_pres.get()) > 21.3 or float(adj_temp.get()) < -164 or float(adj_temp.get()) > -161 :
        adjusted_flow = tk.Label(main_disp, textvariable=adj_flow,bg="white", fg="red")
        adjusted_flow.grid(row=2, column=5)
        adjusted_pres = tk.Label(main_disp, textvariable=adj_pres, bg="white", fg="red")
        adjusted_pres.grid(row=3, column=5)
        adjusted_temp = tk.Label(main_disp, textvariable=adj_temp, bg="white", fg="red")
        adjusted_temp.grid(row=4, column=5)
        #interval close : 구간 차단, 펌프 차단
        cmd = "f"
        py_serial.write(cmd.encode())
        time.sleep(0.1)
    # 3개 모두 정상치라면 다시 정상가동
    else :
        adjusted_flow = tk.Label(main_disp, textvariable=adj_flow, bg="white", fg="blue")
        adjusted_flow.grid(row=2, column=5)
        adjusted_pres = tk.Label(main_disp, textvariable=adj_pres, bg="white", fg="blue")
        adjusted_pres.grid(row=3, column=5)
        adjusted_temp = tk.Label(main_disp, textvariable=adj_temp, bg="white", fg="blue")
        adjusted_temp.grid(row=4, column=5)
        cmd = "e"
        py_serial.write(cmd.encode())
        time.sleep(0.1)

# 수압, 온도 라벨 업데이트
def update_pres_temp() :

    global pres_stat_value
    global temp_stat_value

    pres_stat_value = tk.StringVar()
    temp_stat_value = tk.StringVar()

    if condition :
        pres_stat_value.set(round(random.uniform(15,21.3),2))
        temp_stat_value.set(round(random.uniform(-163,-162),2))

        pres_stat = tk.Label(main_disp, textvariable=pres_stat_value, bg="white", fg="blue")
        pres_stat.grid(row=0, column=3)
        temp_stat = tk.Label(main_disp, textvariable=temp_stat_value, bg="white", fg="blue")
        temp_stat.grid(row=0, column=5)

        main_disp.after(1000,update_pres_temp)

# tkinter GUI 구성
main_disp = tk.Tk()
main_disp.title("CONTROL CONSOLE")
main_disp.geometry("1000x300")
main_disp.resizable(True, True)

#Label, Grid

flow_rate_status_label = tk.Label(main_disp, text="Flow rate(L/M) : ")
flow_rate_status_label.grid(row=0, column=0)

pressure_status_label = tk.Label(main_disp, text="Pressure(MPa) : ")
pressure_status_label.grid(row=0, column=2)

temp_status_label = tk.Label(main_disp, text="Temperature(°C) : ")
temp_status_label.grid(row=0, column=4)

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
main_disp.after(1000, update_pres_temp)

main_disp.mainloop()








