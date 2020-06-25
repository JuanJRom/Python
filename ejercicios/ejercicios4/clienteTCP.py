import socket
import time

class client():
    c = None
    massage = None
    ip = ''
    port = 0

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.c = socket.socket()
        self.c.connect((ip, port))
        print('Connected to the server {} in the port {}' .format(ip, port))
        self.sendF()

    def sendF(self):
        while True:
            msg = 'Test3 send'
            bytes = msg.encode()
            self.c.send(bytes)
            data = self.c.recv(1024)
            print(data)
            time.sleep(2)


client('192.168.0.5', 35495)
