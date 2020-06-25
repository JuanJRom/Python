import socket


class server():
    ip = None
    port = None
    s = None
    client_connection = None
    client_address = None
    counter = 0
    massege = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket()
        print('Server socket has been created')
        self.s.bind((ip, port))
        self.s.listen()
        while True:
            self.client_connection, self.client_address = self.s.accept()
            self.counter += 1
            print('Connection {} accepted of {}'.format(self.counter, self.client_address))
            self.get()

    def get(self):
        self.data = self.client_connection.recv(1024)
        print(self.data)
        if self.data != b'':
            self.sendF('Message received')

    def sendF(self, massege):
        self.massege = massege
        Bytes = self.massege.encode()
        self.client_connection.send(Bytes)
        print('Closed connection')
        self.client_connection.close()


server('192.168.0.5', 35495)
