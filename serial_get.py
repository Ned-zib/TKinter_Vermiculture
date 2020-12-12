from tkinter import simpledialog, messagebox, Tk
import serial
from serial import Serial
import view
from model import data
import sys


class serialData():
    def __init__(self, data):
        self.serial_port = ""
        self.data = data
        self.connected = 0

    def serial_connect(self, root):
        serial_port_name = simpledialog.askstring(
            "", "Serial port (TTY or COM)")
        if serial_port_name:
            print(serial_port_name)
        else:
            root.destroy()
            sys.exit()
        try:
            serial_port = serial.Serial(serial_port_name, 9600)
            self.connected = 1
        except:
            print("Serial Connection Failed")
            messagebox.showerror("Error", "Serial Connection Failed")
            while True:
                try:
                    serial_port_name = simpledialog.askstring(
                        "", "Serial port (TTY or COM)")
                    if serial_port_name:
                        serial_port = serial.Serial(serial_port_name, 9600)
                        self.connected = 1
                    else:
                        root.destroy()
                        sys.exit()
                        break
                    break
                except:
                    print("Serial Connection Failed")
                    messagebox.showerror("Error", "Serial Connection Failed")
        self.serial_port = serial_port

    def get_data(self):
        serial_data = self.serial_port.read()
        if serial_data == b'D':
            data_temp = self.serial_port.read(4)
            data_humi = self.serial_port.read(4)
            data_heat = self.serial_port.read(1)
            data_fan = self.serial_port.read(1)
            data_pump = self.serial_port.read(1)
            self.data.setData(int(data_temp), int(data_humi), int(
                data_fan), int(data_heat), int(data_pump))
            return self.data
