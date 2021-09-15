import threading
from tkinter import *
import tkinter.ttk as ttk
import socket
import pickle
import aa_0_myDB
import os
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("127.0.0.1", 12000)


def start():
    global kill_switch, sub_thread
    kill_switch = threading.Event()
    sub_thread = threading.Thread(target=checkButt)
    sub_thread.start()


def stop():
    kill_switch.set()
    sub_thread.join()


def save():
    vb_1 = var1.get()
    vb_2 = var2.get()
    vb_3 = var3.get()
    vb_4 = var4.get()
    vb_5 = var5.get()
    vb_6 = var6.get()
    vb_7 = var7.get()
    vb_8 = var8.get()
    vb_9 = var9.get()
    vb_10 = var10.get()
    ep1 = e1_p.get()
    ep2 = e2_p.get()
    ep3 = e3_p.get()
    ep4 = e4_p.get()
    ep5 = e5_p.get()
    ep6 = e6_p.get()
    ep7 = e7_p.get()
    ep8 = e8_p.get()
    ep9 = e9_p.get()
    ep10 = e_SPI_1.get()
    er1 = e1_r.get()
    er2 = e2_r.get()
    er3 = e3_r.get()
    er4 = e4_r.get()
    er5 = e5_r.get()
    er6 = e6_r.get()
    er7 = e7_r.get()
    er8 = e8_r.get()
    er9 = e9_r.get()
    er10 = e_SPI_2.get()
    ec1 = e1_c.get()
    ec2 = e2_c.get()
    ec3 = e3_c.get()
    ec4 = e4_c.get()
    ec5 = e5_c.get()
    ec6 = e6_c.get()
    ec7 = e7_c.get()
    ec8 = e8_c.get()
    ec9 = e9_c.get()
    ec10 = e_SPI_3.get()
    eps1 = e1_ps.get()
    eps2 = e2_ps.get()
    eps3 = e3_ps.get()
    eps4 = e4_ps.get()
    eps5 = e5_ps.get()
    eps6 = e6_ps.get()
    eps7 = e7_ps.get()
    eps8 = e8_ps.get()
    eps9 = e9_ps.get()
    eps10 = e_SPI_4.get()
    ei1 = e1_i.get()
    ei2 = e2_i.get()
    ei3 = e3_i.get()
    ei4 = e4_i.get()
    ei5 = e5_i.get()
    ei6 = e6_i.get()
    ei7 = e7_i.get()
    ei8 = e8_i.get()
    ei9 = e9_i.get()
    ei10 = e_SPI_5.get()

    my_list = [vb_1, vb_2, vb_3, vb_4, vb_5, vb_6, vb_7, vb_8, vb_9, vb_10,
               ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8, ep9, ep10,
               er1, er2, er3, er4, er5, er6, er7, er8, er9, er10,
               ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10,
               eps1, eps2, eps3, eps4, eps5, eps6, eps7, eps8, eps9, eps10,
               ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9, ei10]
    pickle.dump(my_list, open('saved_config.dat', 'wb'))


def getTextInput(a_0, a, b, c, d, e):
        vv = int(a.get()) + 1
        # send and receive from server
        rat = int(b.get())
        cmd = int(c.get())
        p_size = int(d.get())
        val = int(e.get())

        config_packet = bytearray()
        config_packet.append(rat)
        config_packet.append(cmd)
        config_packet.append(p_size)
        config_packet.append(val)

        # sending packets to server
        for i in range(1, vv):
            if kill_switch.is_set():
                print("The program has interrupted by the user")
                break
            else:
                message = config_packet
                client_socket.sendto(message, addr)
                try:
                    data, server = client_socket.recvfrom(1024)
                    d1 = str(data)
                    timeEx = time.strftime("%x, %X: ", time.localtime())
                    print(timeEx + a_0 + ' (PACKET ' + str(i) + '): ' + d1)
                    text.insert(END, timeEx + a_0 + ' (PACKET ' + str(i) + ') : ' + d1 + '\n')
                    aa_0_myDB.insertOrReplaceStationData(timeEx, a_0, str(i), d1) #write the report data to the Database "report.db"
                    if a_0 == 'UART_1':
                        lab_1.config(bg='lightgreen')
                    if a_0 == 'UART_2':
                        lab_2.config(bg='lightgreen')
                    if a_0 == 'UART_3':
                        lab_3.config(bg='lightgreen')
                    if a_0 == 'UART_4':
                        lab_4.config(bg='lightgreen')
                    if a_0 == 'UART_5':
                        lab_5.config(bg='lightgreen')
                    if a_0 == 'UART_6':
                        lab_6.config(bg='lightgreen')
                    if a_0 == 'UART_7':
                        lab_7.config(bg='lightgreen')
                    if a_0 == 'UART_8':
                        lab_8.config(bg='lightgreen')
                    if a_0 == 'UART_9':
                        lab_9.config(bg='lightgreen')
                    if a_0 == 'SPI':
                        lab_SPI_in.config(bg='lightgreen')
                except socket.timeout:
                    timeEx = time.strftime("%x, %X: ", time.localtime())
                    print(timeEx + a_0 + ' (PACKET ' + str(i) + '): ' + ' REQUEST TIMED OUT')
                    text.insert(END, timeEx + a_0 + ' (PACKET ' + str(i) + '): ' + ' REQUEST TIMED OUT' + '\n')
                    aa_0_myDB.insertOrReplaceStationData(timeEx, a_0, str(i), "REQUEST TIMED OUT")  # write the report data to the Database "report.db"
                    if a_0 == 'UART_1':
                        lab_1.config(bg='red')
                    if a_0 == 'UART_2':
                        lab_2.config(bg='red')
                    if a_0 == 'UART_3':
                        lab_3.config(bg='red')
                    if a_0 == 'UART_4':
                        lab_4.config(bg='red')
                    if a_0 == 'UART_5':
                        lab_6.config(bg='red')
                    if a_0 == 'UART_6':
                        lab_6.config(bg='red')
                    if a_0 == 'UART_7':
                        lab_7.config(bg='red')
                    if a_0 == 'UART_8':
                        lab_8.config(bg='red')
                    if a_0 == 'UART_9':
                        lab_9.config(bg='red')
                    if a_0 == 'SPI':
                        lab_SPI_in.config(bg='red')


def checkButt():
    if var1.get() == 1:
        name1 = 'UART_1'
        getTextInput(name1, e1_p, e1_r, e1_c, e1_ps, e1_i)
        pass
    if var2.get() == 1:
        name1 = 'UART_2'
        getTextInput(name1, e2_p, e2_r, e2_c, e2_ps, e2_i)
        pass
    if var3.get() == 1:
        name1 = 'UART_3'
        getTextInput(name1, e3_p, e3_r, e3_c, e3_ps, e3_i)
        pass
    if var4.get() == 1:
        name1 = 'UART_4'
        getTextInput(name1, e4_p, e4_r, e4_c, e4_ps, e4_i)
        pass
    if var5.get() == 1:
        name1 = 'UART_5'
        getTextInput(name1, e5_p, e5_r, e5_c, e5_ps, e5_i)
        pass
    if var6.get() == 1:
        name1 = 'UART_6'
        getTextInput(name1, e6_p, e6_r, e6_c, e6_ps, e6_i)
        pass
    if var7.get() == 1:
        name1 = 'UART_7'
        getTextInput(name1, e7_p, e7_r, e7_c, e7_ps, e7_i)
        pass
    if var8.get() == 1:
        name1 = 'UART_8'
        getTextInput(name1, e8_p, e8_r, e8_c, e8_ps, e8_i)
        pass
    if var9.get() == 1:
        name1 = 'UART_9'
        getTextInput(name1, e9_p, e9_r, e9_c, e9_ps, e9_i)
    if var10.get() == 1:
        name1 = 'SPI'
        getTextInput(name1, e_SPI_1, e_SPI_2, e_SPI_3, e_SPI_4, e_SPI_5)
    time.sleep(1)


app = Tk()
app.geometry('1500x800')

br = BooleanVar()
br.set(0)

f_top = LabelFrame(app, text='Status')
f_top_1 = LabelFrame(f_top, text='Power', width=130, height=150)
f_top_2 = LabelFrame(f_top, text='DUP COMM', width=130, height=150)
f_top_3 = LabelFrame(f_top, text='UART', width=130, height=150)
f_top_4 = LabelFrame(f_top, text='SPI', width=130, height=150)
f_top_5 = LabelFrame(f_top, text='I2C', width=130, height=150)

f_power_1 = Label(f_top_1, text='VOLTAGE 1')
f_power_2 = Label(f_top_1, text='VOLTAGE 2')
volt_1 = Label(f_top_1, bg="lightgrey", text="-")
volt_2 = Label(f_top_1, bg="lightgrey", text="-")

f_COM_1 = Label(f_top_2, text='PORT 1')
f_COM_2 = Label(f_top_2, text='PORT 2')
port_1 = Label(f_top_2, bg="lightgrey", text="-")
port_2 = Label(f_top_2, bg="lightgrey", text="-")

f_UART_1 = Label(f_top_3, text='UART 1')
f_UART_2 = Label(f_top_3, text='UART 2')
f_UART_3 = Label(f_top_3, text='UART 3')
f_UART_4 = Label(f_top_3, text='UART 4')
f_UART_5 = Label(f_top_3, text='UART 5')
f_UART_6 = Label(f_top_3, text='UART 6')
f_UART_7 = Label(f_top_3, text='UART 7')
f_UART_8 = Label(f_top_3, text='UART 8')
f_UART_9 = Label(f_top_3, text='UART 9')
f_UART_1.config(font=("Times", "5", "bold"))
f_UART_2.config(font=("Times", "5", "bold"))
f_UART_3.config(font=("Times", "5", "bold"))
f_UART_4.config(font=("Times", "5", "bold"))
f_UART_5.config(font=("Times", "5", "bold"))
f_UART_6.config(font=("Times", "5", "bold"))
f_UART_7.config(font=("Times", "5", "bold"))
f_UART_8.config(font=("Times", "5", "bold"))
f_UART_9.config(font=("Times", "5", "bold"))
f_UART_1.grid(row=0, column=0)
f_UART_2.grid(row=1, column=0)
f_UART_3.grid(row=2, column=0)
f_UART_4.grid(row=3, column=0)
f_UART_5.grid(row=4, column=0)
f_UART_6.grid(row=5, column=0)
f_UART_7.grid(row=6, column=0)
f_UART_8.grid(row=7, column=0)
f_UART_9.grid(row=8, column=0)

lab_1 = Label(f_top_3, bg="lightgrey", text="-")
lab_2 = Label(f_top_3, bg="lightgrey", text="-")
lab_3 = Label(f_top_3, bg="lightgrey", text="-")
lab_4 = Label(f_top_3, bg="lightgrey", text="-")
lab_5 = Label(f_top_3, bg="lightgrey", text="-")
lab_6 = Label(f_top_3, bg="lightgrey", text="-")
lab_7 = Label(f_top_3, bg="lightgrey", text="-")
lab_8 = Label(f_top_3, bg="lightgrey", text="-")
lab_9 = Label(f_top_3, bg="lightgrey", text="-")
lab_1.config(font=("Times", "5", "bold"))
lab_2.config(font=("Times", "5", "bold"))
lab_3.config(font=("Times", "5", "bold"))
lab_4.config(font=("Times", "5", "bold"))
lab_5.config(font=("Times", "5", "bold"))
lab_6.config(font=("Times", "5", "bold"))
lab_7.config(font=("Times", "5", "bold"))
lab_8.config(font=("Times", "5", "bold"))
lab_9.config(font=("Times", "5", "bold"))
lab_1.grid(row=0, column=1, padx=50)
lab_2.grid(row=1, column=1, padx=50)
lab_3.grid(row=2, column=1, padx=50)
lab_4.grid(row=3, column=1, padx=50)
lab_5.grid(row=4, column=1, padx=50)
lab_6.grid(row=5, column=1, padx=50)
lab_7.grid(row=6, column=1, padx=50)
lab_8.grid(row=7, column=1, padx=50)
lab_9.grid(row=8, column=1, padx=50)

SPI_1 = Label(f_top_4, text='   SPI  1 ')
SPI_1.config(font=("Times", "8", "bold"))
SPI_1.grid(row=2, column=0, padx=10, pady=55)
lab_SPI_in = Label(f_top_4, bg="lightgrey", text="-")
lab_SPI_in.config(font=("Times", "8", "bold"))
lab_SPI_in.grid(row=2, column=1, padx=20, pady=55)


# creating in the middle frame Marks - three tabs: UART, SPI, I2C.
f_med = LabelFrame(app, text='Marks')
nb = ttk.Notebook(f_med, width=150, height=250)
f_med_1 = Frame(nb, width=200, height=270)
f_med_2 = Frame(nb, width=200, height=270)
f_med_3 = Frame(nb, width=200, height=270)
nb.add(f_med_1, text='  UARTS ')
nb.add(f_med_2, text='   SPI   ')
nb.add(f_med_3, text='   I2C   ')
nb.pack(fill=BOTH, expand=1, padx=20, pady=20)

l1 = Label(f_med_1, text='COUNT OF PACKETS').grid(row=0, column=1, padx=50)
l2 = Label(f_med_1, text='RATE').grid(row=0, column=2, padx=50)
l3 = Label(f_med_1, text='CMD').grid(row=0, column=3, padx=50)
l4 = Label(f_med_1, text='PACKET`S SIZE').grid(row=0, column=4, padx=50)
l5 = Label(f_med_1, text='INPUT').grid(row=0, column=5, padx=50)

l1_SPI = Label(f_med_2, text='COUNT OF PACKETS').grid(row=0, column=1, padx=50)
l2_SPI = Label(f_med_2, text='RATE').grid(row=0, column=2, padx=50)
l3_SPI = Label(f_med_2, text='CMD').grid(row=0, column=3, padx=50)
l4_SPI = Label(f_med_2, text='PACKET`S SIZE').grid(row=0, column=4, padx=50)
l5_SPI = Label(f_med_2, text='INPUT').grid(row=0, column=5, padx=50)

lab_SPI = Label(f_med_2, text='  SPI   ').grid(row=1, column=1)

var1 = BooleanVar()
var1.set(0)
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()
var10 = BooleanVar()

c1 = Checkbutton(f_med_1, text='UART 1', variable=var1, onvalue=1, offvalue=0)
c1.grid(row=1, column=0)
c2 = Checkbutton(f_med_1, text='UART 2', variable=var2, onvalue=1, offvalue=0)
c2.grid(row=2, column=0)
c3 = Checkbutton(f_med_1, text='UART 3', variable=var3, onvalue=1, offvalue=0)
c3.grid(row=3, column=0)
c4 = Checkbutton(f_med_1, text='UART 4', variable=var4, onvalue=1, offvalue=0)
c4.grid(row=4, column=0)
c5 = Checkbutton(f_med_1, text='UART 5', variable=var5, onvalue=1, offvalue=0)
c5.grid(row=5, column=0)
c6 = Checkbutton(f_med_1, text='UART 6', variable=var6, onvalue=1, offvalue=0)
c6.grid(row=6, column=0)
c7 = Checkbutton(f_med_1, text='UART 7', variable=var7, onvalue=1, offvalue=0)
c7.grid(row=7, column=0)
c8 = Checkbutton(f_med_1, text='UART 8', variable=var8, onvalue=1, offvalue=0)
c8.grid(row=8, column=0)
c9 = Checkbutton(f_med_1, text='UART 9', variable=var9, onvalue=1, offvalue=0)
c9.grid(row=9, column=0)
c10 = Checkbutton(f_med_2, text='SPI', variable=var10, onvalue=1, offvalue=0)
c10.grid(row=1, column=0)

e1_p = Entry(f_med_1, width=15)
e1_p.grid(row=1, column=1, padx=50)
e2_p = Entry(f_med_1, width=15)
e2_p.grid(row=2, column=1, padx=50)
e3_p = Entry(f_med_1, width=15)
e3_p.grid(row=3, column=1, padx=50)
e4_p = Entry(f_med_1, width=15)
e4_p.grid(row=4, column=1, padx=50)
e5_p = Entry(f_med_1, width=15)
e5_p.grid(row=5, column=1, padx=50)
e6_p = Entry(f_med_1, width=15)
e6_p.grid(row=6, column=1, padx=50)
e7_p = Entry(f_med_1, width=15)
e7_p.grid(row=7, column=1, padx=50)
e8_p = Entry(f_med_1, width=15)
e8_p.grid(row=8, column=1, padx=50)
e9_p = Entry(f_med_1, width=15)
e9_p.grid(row=9, column=1, padx=50)

e1_r = Entry(f_med_1, width=15)
e1_r.grid(row=1, column=2, padx=50)
e2_r = Entry(f_med_1, width=15)
e2_r.grid(row=2, column=2, padx=50)
e3_r = Entry(f_med_1, width=15)
e3_r.grid(row=3, column=2, padx=50)
e4_r = Entry(f_med_1, width=15)
e4_r.grid(row=4, column=2, padx=50)
e5_r = Entry(f_med_1, width=15)
e5_r.grid(row=5, column=2, padx=50)
e6_r = Entry(f_med_1, width=15)
e6_r.grid(row=6, column=2, padx=50)
e7_r = Entry(f_med_1, width=15)
e7_r.grid(row=7, column=2, padx=50)
e8_r = Entry(f_med_1, width=15)
e8_r.grid(row=8, column=2, padx=50)
e9_r = Entry(f_med_1, width=15)
e9_r.grid(row=9, column=2, padx=50)

e1_c = Entry(f_med_1, width=15)
e1_c.grid(row=1, column=3, padx=50)
e2_c = Entry(f_med_1, width=15)
e2_c.grid(row=2, column=3, padx=50)
e3_c = Entry(f_med_1, width=15)
e3_c.grid(row=3, column=3, padx=50)
e4_c = Entry(f_med_1, width=15)
e4_c.grid(row=4, column=3, padx=50)
e5_c = Entry(f_med_1, width=15)
e5_c.grid(row=5, column=3, padx=50)
e6_c = Entry(f_med_1, width=15)
e6_c.grid(row=6, column=3, padx=50)
e7_c = Entry(f_med_1, width=15)
e7_c.grid(row=7, column=3, padx=50)
e8_c = Entry(f_med_1, width=15)
e8_c.grid(row=8, column=3, padx=50)
e9_c = Entry(f_med_1, width=15)
e9_c.grid(row=9, column=3, padx=50)

e1_ps = Entry(f_med_1, width=15)
e1_ps.grid(row=1, column=4, padx=50)
e2_ps = Entry(f_med_1, width=15)
e2_ps.grid(row=2, column=4, padx=50)
e3_ps = Entry(f_med_1, width=15)
e3_ps.grid(row=3, column=4, padx=50)
e4_ps = Entry(f_med_1, width=15)
e4_ps.grid(row=4, column=4, padx=50)
e5_ps = Entry(f_med_1, width=15)
e5_ps.grid(row=5, column=4, padx=50)
e6_ps = Entry(f_med_1, width=15)
e6_ps.grid(row=6, column=4, padx=50)
e7_ps = Entry(f_med_1, width=15)
e7_ps.grid(row=7, column=4, padx=50)
e8_ps = Entry(f_med_1, width=15)
e8_ps.grid(row=8, column=4, padx=50)
e9_ps = Entry(f_med_1, width=15)
e9_ps.grid(row=9, column=4, padx=50)

e1_i = Entry(f_med_1, width=15)
e1_i.grid(row=1, column=5, padx=50)
e2_i = Entry(f_med_1, width=15)
e2_i.grid(row=2, column=5, padx=50)
e3_i = Entry(f_med_1, width=15)
e3_i.grid(row=3, column=5, padx=50)
e4_i = Entry(f_med_1, width=15)
e4_i.grid(row=4, column=5, padx=50)
e5_i = Entry(f_med_1, width=15)
e5_i.grid(row=5, column=5, padx=50)
e6_i = Entry(f_med_1, width=15)
e6_i.grid(row=6, column=5, padx=50)
e7_i = Entry(f_med_1, width=15)
e7_i.grid(row=7, column=5, padx=50)
e8_i = Entry(f_med_1, width=15)
e8_i.grid(row=8, column=5, padx=50)
e9_i = Entry(f_med_1, width=15)
e9_i.grid(row=9, column=5, padx=50)

e_SPI_1 = Entry(f_med_2, width=15)
e_SPI_1.grid(row=1, column=1, padx=50)
e_SPI_2 = Entry(f_med_2, width=15)
e_SPI_2.grid(row=1, column=2, padx=50)
e_SPI_3 = Entry(f_med_2, width=15)
e_SPI_3.grid(row=1, column=3, padx=50)
e_SPI_4 = Entry(f_med_2, width=15)
e_SPI_4.grid(row=1, column=4, padx=50)
e_SPI_5 = Entry(f_med_2, width=15)
e_SPI_5.grid(row=1, column=5, padx=50)

# position of Frame
f_top.pack(fill=X, expand=False, padx=10, pady=10)
f_top_1.pack(side=LEFT, padx=30, pady=10)
f_top_1.pack_propagate(False)
f_top_2.pack(side=LEFT, padx=30, pady=10)
f_top_3.pack(side=LEFT, padx=30, pady=10)
f_top_3.pack_propagate(False)
f_top_4.pack(side=LEFT, padx=30, pady=10)
f_top_5.pack(side=LEFT, padx=30, pady=10)

f_med.pack(fill=X, expand=False, padx=10, pady=10)
f_power_1.place(rely=0.2)
f_power_2.place(rely=0.5)
volt_1.place(relx=0.6, rely=0.2)
volt_2.place(relx=0.6, rely=0.5)
f_COM_1.place(rely=0.2)
f_COM_2.place(rely=0.5)
port_1.place(relx=0.6, rely=0.2)
port_2.place(relx=0.6, rely=0.5)


# *CONSOLE*
messages_frame = LabelFrame(app, text='Console', height=100)
messages_frame.pack_propagate(False)
messages_frame.pack(fill=X, padx=10, pady=10)
text = Text(messages_frame, fg='Black', width=140, height=90, font=("Consolas", 11), bg='white')
text.pack(fill=X, padx=5, ipady=5)

scr = Scrollbar(text, command=text.yview)
scr.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scr.set)

# *START-STOP*
frame_StSt = LabelFrame(app, height=100)
frame_StSt.pack(fill=X, expand=0.5, padx=10, pady=10)

st = Button(frame_StSt, text='START', width=12, height=4)
st.bind('<Button-1>', lambda j: threading.Thread(target=start).start())
stp = Button(frame_StSt, text='STOP', width=12, height=4)
stp.bind('<Button-1>', lambda j: threading.Thread(target=stop).start())
sv = Button(frame_StSt, text='SAVE', width=12, height=4, command=save)
st.place(relx=0.30, rely=0.5, anchor=CENTER)
stp.place(relx=0.50, rely=0.5, anchor=CENTER)
sv.place(relx=0.70, rely=0.5, anchor=CENTER)

# write configuration to file
if not os.path.isfile('saved_config.dat'):
    with open('saved_config.dat', 'wb') as file:
        pickle.dump(1, file)
else:
    with open('saved_config.dat', "rb") as in_f:
        try:
            vb_1, vb_2, vb_3, vb_4, vb_5, vb_6, vb_7, vb_8, vb_9, vb_10, \
            ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8, ep9, ep10, \
            er1, er2, er3, er4, er5, er6, er7, er8, er9, er10, \
            ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10, \
            eps1, eps2, eps3, eps4, eps5, eps6, eps7, eps8, eps9, eps10, \
            ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9, ei10 = pickle.load(in_f)

            var1.set(vb_1)
            var2.set(vb_2)
            var3.set(vb_3)
            var4.set(vb_4)
            var5.set(vb_5)
            var6.set(vb_6)
            var7.set(vb_7)
            var8.set(vb_8)
            var9.set(vb_9)
            var10.set(vb_10)
            e1_p.insert(0, ep1)
            e2_p.insert(0, ep2)
            e3_p.insert(0, ep3)
            e4_p.insert(0, ep4)
            e5_p.insert(0, ep5)
            e6_p.insert(0, ep6)
            e7_p.insert(0, ep7)
            e8_p.insert(0, ep8)
            e9_p.insert(0, ep9)
            e_SPI_1.insert(0, ep10)
            e1_r.insert(0, er1)
            e2_r.insert(0, er2)
            e3_r.insert(0, er3)
            e4_r.insert(0, er4)
            e5_r.insert(0, er5)
            e6_r.insert(0, er6)
            e7_r.insert(0, er7)
            e8_r.insert(0, er8)
            e9_r.insert(0, er9)
            e_SPI_2.insert(0, er10)
            e1_c.insert(0, ec1)
            e2_c.insert(0, ec2)
            e3_c.insert(0, ec3)
            e4_c.insert(0, ec4)
            e5_c.insert(0, ec5)
            e6_c.insert(0, ec6)
            e7_c.insert(0, ec7)
            e8_c.insert(0, ec8)
            e9_c.insert(0, ec9)
            e_SPI_3.insert(0, ec10)
            e1_ps.insert(0, eps1)
            e2_ps.insert(0, eps2)
            e3_ps.insert(0, eps3)
            e4_ps.insert(0, eps4)
            e5_ps.insert(0, eps5)
            e6_ps.insert(0, eps6)
            e7_ps.insert(0, eps7)
            e8_ps.insert(0, eps8)
            e9_ps.insert(0, eps9)
            e_SPI_4.insert(0, eps10)
            e1_i.insert(0, ei1)
            e2_i.insert(0, ei2)
            e3_i.insert(0, ei3)
            e4_i.insert(0, ei4)
            e5_i.insert(0, ei5)
            e6_i.insert(0, ei6)
            e7_i.insert(0, ei7)
            e8_i.insert(0, ei8)
            e9_i.insert(0, ei9)
            e_SPI_5.insert(0, ei10)

        except Exception:
            pass

app.mainloop()
