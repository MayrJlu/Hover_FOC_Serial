import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.ttk import Spinbox
from tkinter import Canvas
from tkinter import Text
from tkinter.messagebox import showinfo
import binascii
import serPort
#import saveLoad

##import screenRecogniser

# scrRcgnsr = screenRecogniser.screenRecogniserClass()





class TkGuiClass:

    def __init__(self):
        print("TkGuiClass __init__")

        self.ser = serPort.SrlPrtClass()
        self.ports = self.ser.serial_ports()
        print("availible ports" + str(self.ports))
        self.window = tk.Tk()
        self.window.title("Hover_FOC_Serial")

        self.panel = tk.Canvas(width=640, height=320, bg='white')
        self.panel.grid()
        self.panel.create_oval(10, 10, 310, 310, fill="yellow", outline="green", width=5)
        self.panel.create_text(160, 160,
              text="0 rpm",
              font="Verdana 24")

        self.lblSelectPort = tk.Label(self.window, text="select port")
        self.lblSelectPort.grid(column=0, row=0)

        self.comboSelectPortSer = Combobox(self.window)
        self.comboSelectPortSer['values'] = (self.ports + ["select port"])
        self.comboSelectPortSer.current(1)
        self.comboSelectPortSer.bind("<<ComboboxSelected>>", self.callbackFuncClient)
        self.comboSelectPortSer.grid(column=1, row=0)

        self.lblBaud = tk.Label(self.window, text="------")
        self.lblBaud.grid(column=2, row=0)

        self.buttonConnectSerial = tk.Button(self.window, text="Connect", command=self.connect_Serial)
        self.buttonConnectSerial.grid(column=3, row=0)

        self.buttonWriteSerial = tk.Button(self.window, text="Write", command=self.connect_Serial)
        self.buttonWriteSerial.grid(column=4, row=0)

        self.buttonReadSerial = tk.Button(self.window, text="Read", command=self.connect_Serial)
        self.buttonReadSerial.grid(column=5, row=0)
        
        self.lblDataToSend = tk.Label(self.window, text="data to send")
        self.lblDataToSend.grid(column=0, row=1)

        self.textBox = tk.Text(self.window, height = 1 , width = 25) 
        self.textBox.grid(column=1, row=1) 
        # start main loop
        self.window.mainloop()


    def callbackFuncClient(self, event):
        print("New Element Selected")
        print(self.ser.portsAvalable[self.comboSelectPortSer.current()])
        #print(self.serClient)

    def connect_Serial(self):
        print("connect serial", self.ser.portsAvalable[self.comboSelectPortSer.current()])
        self.ser.portSel = self.comboSelectPortSer.current()
        self.ser.serial_open(self.ser.portSel)
        self.ser.serial_write(self.textBox.get(1.0))
        self.ser.serial_read()
        print("dbg")
