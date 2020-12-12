from tkinter import Tk
from model import data
from view import View
from serial_get import serialData


class Controller():
    def __init__(self):
        self.root = Tk()
        self.root.title("Vermiculture")
        self.data = data(0, 0, 0, 0, 0)
        self.serial_data = serialData(self.data)
        self.view = View(self.root)

    def run(self):
        self.serial_data.serial_connect(self.root)
        self.root.after(1, self.set_data())
        self.root.mainloop()

    def set_data(self):
        try:
            self.data = self.serial_data.get_data()
            if self.data:
                self.view.cleanFields()
                self.view.writeFields(self.data, self.root)
        except:
            pass
        self.root.after(1, self.set_data())
        

if __name__ == "__main__":
    # running controller function
    control = Controller()
    control.run()
