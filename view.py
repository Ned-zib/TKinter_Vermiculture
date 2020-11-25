from tkinter import *
from tkinter import simpledialog, messagebox
from model import *
import serial
from serial import Serial
# import controller
import sys

# Var for serial port
serial_port_name = ""
serial_port = Serial
# Field declarations
temp_field = Entry
humi_field = Entry
fan_field = Entry
heat_field = Entry
pump_field = Entry


class View():
    def __init__(self, root):
        # BG Color
        root.configure(bg="white")

        # master is a frame inside the main window
        self.master = LabelFrame(root, text="Vermiculture", font=('arial', 14, 'bold'), width=1000, bg='white')
        self.master.pack(side=BOTTOM)

        # input_var is a frame inside the master located at the left to organize the inputs
        self.input_var = LabelFrame(self.master, text="Input", font=('arial', 12), bg='white')
        self.input_var.pack(side=LEFT)

        self.temp_label = Message(self.input_var, text="--Temperature--", width=600, bg='white')
        self.temp_label.pack()
        self.temp_field = Entry(self.input_var, width=7, bg='white')
        self.temp_field.pack()

        self.humi_label = Message(self.input_var, text="--Humidity--", width=600, bg='white')
        self.humi_label.pack()
        self.humi_field = Entry(self.input_var, width=7, bg='white')
        self.humi_field.pack()

        # output_var is a frame inside the master located at the right to organize the outputs
        self.output_var = LabelFrame(self.master, text="Output", font=('arial', 12), bg='white')
        self.output_var.pack(side=LEFT)

        self.fan_label = Message(self.output_var, text="--Fan--", width=600, bg='white')
        self.fan_label.pack(side=TOP)
        self.fan_field = Entry(self.output_var, width=15, bg='white')
        self.fan_field.pack(side=TOP)

        self.heat_label = Message(self.output_var, text="--Heaters--", width=600, bg='white')
        self.heat_label.pack(side=TOP)
        self.heat_field = Entry(self.output_var, width=15, bg='white')
        self.heat_field.pack(side=TOP)

        self.pump_label = Message(self.output_var, text="--Pump--", width=600, bg='white')
        self.pump_label.pack(side=TOP)
        self.pump_field = Entry(self.output_var, width=15, bg='white')
        self.pump_field.pack(side=TOP)

        # Root Update and BlockSize
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        root.maxsize(root.winfo_width(), root.winfo_height())

    def writeFields(self, data):
        print("Writing fields")
        # Write Data
        self.temp_field.insert(1, data.getTemperature())
        self.temp_field.insert(4, " C°    ")

        self.humi_field.insert(1, data.getHumidity())
        self.humi_field.insert(4, " %    ")

        if data.getFan() == b'1':
            self.heat_field.insert(1, "Heating")
        else:
            self.heat_field.insert(1, "Off")

        if data.getHeater() == b'1':
            self.fan_field.insert(1, "Cooling")
        else:
            self.fan_field.insert(1, "Normal")
        if data.getHeater() == b'2':
            self.fan_field.delete(0, 11)
            self.heat_field.delete(0, 11)
            self.fan_field.insert(1, "Evaporating")
            self.heat_field.insert(1, "Evaporating")

        if data.getPump() == b'1':
            self.pump_field.insert(1, "On")
        else:
            self.pump_field.insert(1, "Off")
        print(str(data.getTemperature()) + "||" + str(data.getHumidity()) + "||" + str(data.getFan()) + "||" + str(
            data.getHeater()) + "||" + str(data.getPump()))
        print("Write fields method end")

    def cleanFields(self):
        print("--------------------------------------------")
        print("Cleaning fields")
        # Clean Fields
        self.temp_field.delete(0, 11)
        self.humi_field.delete(0, 11)
        self.fan_field.delete(0, 11)
        self.heat_field.delete(0, 11)
        self.pump_field.delete(0, 11)
