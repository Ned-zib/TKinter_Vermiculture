from tkinter import *
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.commondialog import Dialog
from tkinter.filedialog import *
import serial

e = serial.Serial("COM9", 9600)
print("Conectado")
root= Tk()

def salir():
    e.close()
    root.destroy()

root.configure(bg="white")

root.title('Lombricultivo')
salir=Button(root,text="Salir",width=10,height=1,command=salir)
salir.pack(side=BOTTOM)

master=LabelFrame(root,text="Lombricultivo",font=('arial',14,'bold'),width=1000,bg='white')
master.pack(side=BOTTOM)
entradas= LabelFrame(master,text="Entradas",font=('arial',12),bg='white')
entradas.pack(side=LEFT)
lbl1=Message(entradas,text="Temperatura-------------------",width=300,bg='white')
lbl1.pack()
temp = Entry(entradas,width=7,bg='white')
temp.pack()
lbl1=Message(entradas,text="Humedad-----------------------",width=300,bg='white')
lbl1.pack()
hum = Entry(entradas,width=7,bg='white')
hum.pack()
barra=Frame(master,bg='white')
barra.pack(side= BOTTOM)
lbls=Message(barra,bg='white',text=" ")
lbls.pack()

salidas= LabelFrame(master,text="Salidas",font=('arial',12),bg='white')
salidas.pack(side=LEFT)
lbl2=Message(salidas, text="Ventiladores------------------",width=300,bg='white')
lbl2.pack(side=TOP)
ven = Entry(salidas,width=15,bg='white')
ven.pack(side=TOP)
lbl3=Message(salidas, text="Resistencias------------------",width=300,bg='white')
lbl3.pack(side=TOP)
res = Entry(salidas,width=15,bg='white')
res.pack(side=TOP)
lbl4=Message(salidas, text="Bomba-------------------------",width=300,bg='white')
lbl4.pack(side=TOP)
bom = Entry(salidas,width=15,bg='white')
bom.pack(side=TOP)

def readSerial():
     a=e.read()
     if a==b'D':
         temp.delete(0,11)
         hum.delete(0,11)
         ven.delete(0,11)
         res.delete(0,11)
         bom.delete(0,11)
         a=e.read(4)
         b=e.read(4)
         c=e.read(1)
         d=e.read(1)
         t=e.read(1)
         temp.insert(1, a)
         temp.insert(4," C°")
         hum.insert(1, b)
         hum.insert(4," %")
         if c==b'1':
             res.insert(1,"Calentando")
         else:
             res.insert(1,"Apagado")
         if d==b'1':
             ven.insert(1,"Enfriando")
         else:
             ven.insert(1,"Normal")
         if d==b'2':
             ven.delete(0,11)
             res.delete(0,11)
             ven.insert(1,"Evaporando")
             res.insert(1,"Evaporando")
         if t==b'1':
             bom.insert(1,"Encendida")
         else:
             bom.insert(1,"Apagada")
       
         print(a+b)
     root.after(10, readSerial)
root.after(100, readSerial)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())
root.mainloop()
