import tkinter
from tkinter import *
from tkinter import messagebox as mb

def SPI():
    root.destroy()
    newWindow = tkinter.Tk()
    newWindow.title("SPI")
    newWindow.geometry('400x400+800+300')
    button_1 = tkinter.Button(newWindow, text="IMU Demo", width=10, height=5, command=create_IMU_Demo)
    button_2 = tkinter.Button(newWindow, text="User Input", width=10, height=5)
    button_1.pack(side='left', anchor='e', expand=True, padx=50, pady=50)
    button_2.pack(side='right', anchor='w', expand=True, padx=50, pady=50)
    newWindow.grab_set()
    newWindow.focus_set()
    newWindow.mainloop()

def create_IMU_Demo():
    new_IMU = Tk()
    new_IMU.title("Data for sending")
    new_IMU.geometry('400x400+800+300')

    lab1 = Label(new_IMU, text="Enter count of packets (from 1 to 254)")
    lab2 = Label(new_IMU, text="Enter transmission frequency (from 1 to 254)")
    e1 = Entry(new_IMU, width=35)
    e2 = Entry(new_IMU, width=35)
    butt1 = Button(new_IMU, text="SEND")
    butt2 = Button(new_IMU, text="SEND")
    lab3res = Label(new_IMU, text="Result1", fg='red')
    lab4res = Label(new_IMU, text="Result2", fg='red')

    lab1.place(x=10, y=20)
    e1.place(x=10, y=50)
    butt1.place(x=70, y=85)
    lab3res.place(x=10, y=115)
    lab2.place(x=10, y=150)
    e2.place(x=10, y=180)
    butt2.place(x=70, y=215)
    lab4res.place(x=10, y=245)

    def to_label1(event):
        val1 = e1.get()
        if not val1.isdigit():
            # mb.showerror("ERROR", "a value1 must be number")
            lab3res.configure(text="ERROR, a COUNT_OF_PACKETS must be number\n Enter new value!!!", fg='red')
        elif int(val1) < 1 or int(val1) > 254:
            # mb.showerror("ERROR", "Enter value_1 from 1 to 254")
            lab3res.configure(text="ERROR, a COUNT_OF_PACKETS must be from 1 to 254\n Enter new value!!!", fg='red')
        else:
            lab3res.configure(text="a COUNT_OF_PACKETS: " + val1 + " is sent", fg='blue')

    def to_label2(event):
        val2 = e2.get()
        if not val2.isdigit():
            # mb.showerror("ERROR", "a value1 must be number")
            lab4res.configure(text="ERROR, TRANSMISSION_FREQUENCY must be number\n Enter new value!!!", fg='red')
        elif int(val2) < 1 or int(val2) > 254:
            # mb.showerror("ERROR", "Enter number1 from 1 to 254")
            lab4res.configure(text="ERROR, TRANSMISSION_FREQUENCY must be from 1 to 254\n Enter new value!!!", fg='red')
        else:
            lab4res.configure(text="TRANSMISSION_FREQUENCY: " + val2 + " is sent", fg='blue')

    e1.bind('<Return>', to_label1)
    e2.bind('<Return>', to_label2)
    butt1.bind('<Button-1>', to_label1)
    butt2.bind('<Button-1>', to_label2)
    #new_IMU.mainloop()

def UART():
    root.destroy()
    RXTX = tkinter.Tk()
    RXTX.title("UART")
    RXTX.geometry('400x400+800+300')
    lab_port = Label(RXTX, text="Сhoose the port you want to use: ", font="Arial 16")
    lab_port.place(x=30, y=70)
    but_UART_1 = Button(RXTX, text="1", width=5, height=3, command=create_IMU_Demo)
    but_UART_1.place(x=10, y=160)
    but_UART_2 = Button(RXTX, text="2", width=5, height=3, command=create_IMU_Demo)
    but_UART_2.place(x=65, y=160)
    but_UART_3 = Button(RXTX, text="3", width=5, height=3, command=create_IMU_Demo)
    but_UART_3.place(x=120, y=160)
    but_UART_4 = Button(RXTX, text="4", width=5, height=3, command=create_IMU_Demo)
    but_UART_4.place(x=175, y=160)
    but_UART_5 = Button(RXTX, text="5", width=5, height=3, command=create_IMU_Demo)
    but_UART_5.place(x=225, y=160)
    but_UART_6 = Button(RXTX, text="6", width=5, height=3, command=create_IMU_Demo)
    but_UART_6.place(x=280, y=160)
    but_UART_7 = Button(RXTX, text="7", width=5, height=3, command=create_IMU_Demo)
    but_UART_7.place(x=345, y=160)

root = Tk()
root.title("Welcome to App")
root.geometry('400x400+800+300')
lab_device = Label(text="Сhoose the device you want to use: ", font="Arial 16")
lab_device.place(x=30, y=70)
but1 = Button(root, text='UART', width=10, height=5, command=UART)
but1.pack(side='left', anchor='e', expand=True, padx=70, pady=50)
but2 = Button(root, text='SPI', width=10, height=5, command=SPI)
but2.pack(side='right', anchor='w',  padx=50, pady=50)
root.mainloop()