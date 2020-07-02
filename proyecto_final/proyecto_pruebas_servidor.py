import socket as s
import time

serverSocket = s.socket()
print('Se ha creado el socket del servidor')

ip = ''
port = 35491

serverSocket.bind((ip, port))
print(f'Esperando la conexion')
serverSocket.listen()
salir = False

pktCount = 0

while not salir:
    (clienteCon, clientAddr) = serverSocket.accept()

    print('Esperando paquetes')
    f2 = open('copiazip.zip', 'wb')
    while True:
        data = clienteCon.recv(1024)

        pktCount += 1
        if pktCount != 1 and pktCount != 2 and pktCount != 8:
            f2.write(data)
        print(f'[{pktCount}] Recibi un mensaje: {data} de {clientAddr}')

        msg = 'Enviar Archivo .zip!'

        clienteCon.send(msg.encode())
    f2.close()
    print('Conexion cerrada')
    clienteCon.close()

