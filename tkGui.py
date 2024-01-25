import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.ttk import Spinbox
from tkinter.messagebox import showinfo
#import serial
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

        self.lblClient = tk.Label(self.window, text="select port")
        self.lblClient.grid(column=0, row=0)

        self.comboClientSer = Combobox(self.window)
        self.comboClientSer['values'] = (self.ports + ["select port"])
        self.comboClientSer.current(1)
        self.comboClientSer.bind("<<ComboboxSelected>>", self.callbackFuncClient)
        self.comboClientSer.grid(column=1, row=0)

        self.lblServer = tk.Label(self.window, text="------")
        self.lblServer.grid(column=2, row=0)

        self.buttonConnectSerial = tk.Button(self.window, text="Read from server", command=self.connect_Serial)
        self.buttonConnectSerial.grid(column=3, row=0)
        # start main loop
        self.window.mainloop()


    def callbackFuncClient(self, event):
        print("New Element Selected")
        print(self.ser.portsAvalable[self.comboClientSer.current()])
        #print(self.serClient)

    def connect_Serial(self):
        print("connect serial", self.ser.portsAvalable[self.comboClientSer.current()])
        self.ser.portSel = self.comboClientSer.current()
        self.ser.serial_open(self.ser.portSel)
