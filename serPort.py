import serial
import glob
import sys
import threading
import queue
#import tkGui
import hoverCommands

#q = queue.Queue()




class SrlPrtClass:
    def __init__(self):

        print("SrlPrtClass __init__")
        self.portsAvalable = self.serial_ports()
        self.portSel = []
        self.r_p_m = 0

#        self.hvr = hoverCommands.HvrCmmndsClass()
#        self.hvr.get_parametr(3)

    #################################################
    # function for finding all connected serial ports
    # returns : COM* or /dev/tty*
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    #
    #
    #################################################


################## open serial port
    def serial_open(self, portNumber):
        print("connect serial", self.portsAvalable[portNumber])
        print(portNumber)
        self.opendPort = serial.Serial((self.portsAvalable[portNumber]),
                                           baudrate=115200,
                                           stopbits=serial.STOPBITS_ONE,
                                           bytesize=serial.EIGHTBITS
                                           )


    def serial_write(self, inString):
        self.opendPort.write(bytes(inString, encoding="raw_unicode_escape"))

################# thread to read serial
    def serial_read(self):
        self.srlThread = threading.Thread(target = self.read_byte, daemon = True)
        self.srlThread.start()
        #self.item = q.get()
    def read_byte(self):
        while True:
            self.bufer = self.opendPort.readline()
            self.bufLen = len(self.bufer)
            if self.bufLen == 18:
                self.r_p_m = self.bufer[11]
                gui.hvrCmd.hvrRpm = self.r_p_m
                print(self.r_p_m)
            #q.task_done()
