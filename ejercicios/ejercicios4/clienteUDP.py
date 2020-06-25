import socket
import time


class cliente():
    ip = ''
    port = 0
    addr = None
    data = None
    massage = ''

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = self.ip, self.port
        self.sendF('Client message')

    def sendF(self, massage):
        while True:
            self.massage = massage
            bytes = self.massage.encode()
            self.c.sendto(bytes, self.addr)
            self.get()

    def get(self):
        self.data, self.addr = self.c.recvfrom(1024)
        print('Received: {} de {}'.format(self.data, self.addr))
        time.sleep(2)


cliente('192.168.0.5', 35495)
