import serial
import glob
import sys
#import threading

class SrlPrtClass:
    def __init__(self):

        print("SrlPrtClass __init__")
        self.portsAvalable = self.serial_ports()
        self.portSel = []


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

    def serial_open(self, portNumber):
        print("connect serial", self.portsAvalable[portNumber])
        print(portNumber)
        self.opendPort = serial.Serial((self.portsAvalable[portNumber]),
                                           baudrate=9600,
                                           stopbits=serial.STOPBITS_ONE,
                                           bytesize=serial.EIGHTBITS
                                           )


    def serial_write(self):
        self.req = bytes([0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
        self.opendPort.write(self.req)

    def serial_read(self, nOfBytes):
        self.start = bytes(self.opendPort.read(nOfBytes))
        self.length = self.start[1]
        # self.length = int.from_bytes(self.start[1], byteorder='big')

        self.bufer = bytes()
        self.stop = 1
        while (self.stop):
            self.ansver = bytes(serial.read(1))
            if self.ansver != bytes([0xde]):
                self.bufer += self.ansver
            else:
                self.stop = 0
# def serial_read();
