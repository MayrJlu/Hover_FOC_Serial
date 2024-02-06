import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.ttk import Spinbox
from tkinter import Canvas
from tkinter import Text
from tkinter.messagebox import showinfo
import binascii
from math import *
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

        self.panel = tk.Canvas(width=640, height=320, bg='black')
        self.panel.grid()
        self.panel.create_oval(10, 10, 310, 310, fill="black", outline="gray", width=5)
        self.panel.create_oval(100, 100, 220, 220, fill="black", outline="gray", width=5)
        self.calc_div_lines(13, 260, 210)
        self.calc_rpm_line(1160)

        #self.lblSelectPort = tk.Label(self.window, text="select port")
        #self.lblSelectPort.grid(column=0, row=0)

        self.comboSelectPortSer = Combobox(self.window)
        self.comboSelectPortSer['values'] = (self.ports + ["select port"])
        self.comboSelectPortSer.current(1)
        self.comboSelectPortSer.bind("<<ComboboxSelected>>", self.callbackFuncSelectPortSer)
        self.comboSelectPortSer.grid(column=1, row=0)

        #self.lblBaud = tk.Label(self.window, text="------")
        #self.lblBaud.grid(column=2, row=0)

        self.buttonConnectSerial = tk.Button(self.window, text="Connect", command=self.connect_Serial)
        self.buttonConnectSerial.grid(column=1, row=1)

        self.buttonWriteSerial = tk.Button(self.window, text="Write", command=self.write_Serial)
        self.buttonWriteSerial.grid(column=1, row=2)
        
        self.lblDataToSend = tk.Label(self.window, text="data to send")
        self.lblDataToSend.grid(column=0, row=1)

        self.textBox = tk.Text(self.window, height = 1 , width = 25) 
        self.textBox.grid(column=0, row=2) 
        # start main loop
        self.window.mainloop()


    def callbackFuncSelectPortSer(self, event):
        print("New Element Selected")
        print(self.ser.portsAvalable[self.comboSelectPortSer.current()])
        #print(self.serClient)

    def connect_Serial(self):
        print("connect serial", self.ser.portsAvalable[self.comboSelectPortSer.current()])
        self.ser.portSel = self.comboSelectPortSer.current()
        self.ser.serial_open(self.ser.portSel)
        self.ser.serial_read()

    def write_Serial(self):
        self.txt = self.textBox.get(1.0, 'end-1c')
        print("write serial", self.txt)
        self.ser.serial_write(self.txt)
        print("dbg")

    def calc_rpm_line(self, rpm):
        self.maxRpm = 1200
        self.maxAngle = 240
        self.minVal = 210
        # max kmh = 60
        self.rpmDegree = rpm/(self.maxRpm/self.maxAngle)
        print(self.rpmDegree)
        self.angle = radians(self.minVal - self.rpmDegree)
        print(self.angle)
        self.rOut = 150
        self.rIn = 60
        self.x1 = 160
        self.y1 = 160
        self.x2 = 310
        self.y2 = 160
        self.sinA = sin(self.angle)
        self.cosA = cos(self.angle)
        print(self.sinA)
        print(self.cosA)
        self.x1 = self.x1 - self.rIn
        self.x1 = self.x1 + self.cosA * self.rIn + self.rIn
        self.y1 = self.y1 - self.sinA * self.rIn
        self.x2 = self.x2 + self.cosA * self.rOut - self.rOut
        self.y2 = self.y2 - self.sinA * self.rOut
        self.panel.create_text(160, 160,
              text="1200\n rpm",
              font="Verdana 24",
              fill="white")

        self.panel.create_line(self.x1, self.y1, self.x2, self.y2, fill="blue", width=5)
        #return (self.x1, self.y1, self.x2, self.y2)

    def calc_div_lines(self, nLines, nDegrees, minMarkDegrees):
        self.maxFull = 360
        self.maxAngle = nDegrees
        self.minVal = minMarkDegrees#210
        # max kmh = 60
        self.lineDegree = (self.maxAngle/nLines)
        print(self.lineDegree)
        i = 0
        while i < nLines:
            self.angle = radians(self.minVal - i * self.lineDegree)
            i = i + 1
            print(self.angle)
            self.rOut = 150
            self.rIn = 130
            self.x1 = 160
            self.y1 = 160
            self.x2 = 310
            self.y2 = 160
            self.sinA = sin(self.angle)
            self.cosA = cos(self.angle)
            print(self.sinA)
            print(self.cosA)
            self.x1 = self.x1 - self.rIn
            self.x1 = self.x1 + self.cosA * self.rIn + self.rIn
            self.y1 = self.y1 - self.sinA * self.rIn
            self.x2 = self.x2 + self.cosA * self.rOut - self.rOut
            self.y2 = self.y2 - self.sinA * self.rOut
            self.panel.create_line(self.x1, self.y1, self.x2, self.y2, fill="gray", width=3)
