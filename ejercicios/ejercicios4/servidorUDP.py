import socket

class server():
    s = None
    ip = ''
    port = 0
    count = 0
    address = None
    data = None
    massage = ''

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Server socket has been created')
        self.s.bind((ip, port))
        print('Waiting for packagess')
        self.get()

    def get(self):
        while True:
            self.data, self.address = self.s.recvfrom(1024)
            self.count += 1
            print('[{}] Received a message: {} of {}'.format(self.count, self.data, self.address))
            self.massage = 'Message received'
            self.s.sendto(self.massage.encode(), self.address)

server('192.168.0.5', 35495)