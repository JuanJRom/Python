from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import Slot
from proyecto_final.ui_proyecto import Ui_proyecto
import socket as s
import sys
import time
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Estudiante:
    _nombre = ''
    _correo = ''
    _contrasena = ''

    def __init__(self, nombre, correo, contrasena):
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena

    def __str__(self):
        return f'Nombre: {self._nombre}\n' \
               f'Correo: {self._correo}\n'

    def nombre(self):
        return self._nombre

    def correo(self):
        return self._correo

    def contrasena(self):
        return self._contrasena

    def actualizarNombre(self, nombre=None):
        if nombre:
            self._nombre = nombre
            return True
        else:
            return False

    def actualizarCorreo(self, correo=None):
        if correo:
            self._correo = correo
            return True
        else:
            return False

    def actualizarContrasena(self, contrasena=None):
        if contrasena:
            self._contrasena = contrasena
            return True
        else:
            return False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_proyecto()
        self.ui.setupUi(self)
        self.setWindowTitle('Cliente<Juan Romero>')
        self.ui.label_7.setText('Desconectado')
        self.error = QMessageBox()
        self.file = None
        self.student = None
        self.cliente = None

        self.ui.pushButtonConect.clicked.connect(self.connect_server)
        self.ui.pushButtonSendEstudent.clicked.connect(self.send_student)
        self.ui.pushButtonSearsFile.clicked.connect(self.open_file)
        self.ui.pushButtonSendFile.clicked.connect(self.send_file)

    def show_error(self, message):
        self.error.setText(message)
        self.error.setIcon(QMessageBox.Warning)
        self.error.exec_()

    @Slot()
    def connect_server(self):
        if self.ui.pushButtonConect.text() == 'Conectar':
            try:
                self.cliente = s.socket()
                self.cliente.connect((self.ui.lineEditIP.text(), int(self.ui.lineEditPort.text())))
                self.ui.label_7.setText('Conectado')
                self.ui.pushButtonConect.setText('Desconectar')
            except:
                e = sys.exc_info()[1]
                self.show_error(str(e))
        elif self.ui.pushButtonConect.text() == 'Desconectar':
            self.cliente.close()
            self.ui.label_7.setText('Desconectado')
            self.ui.pushButtonConect.setText('Conectar')

    @Slot()
    def send_student(self):
        temp = Estudiante(self.ui.lineEditName.text(), self.ui.lineEditEmail.text(), self.ui.lineEditPassword.text())
        self.student = pickle.dumps(temp)
        print(self.student)
        try:
            self.cliente.send(self.student)
        except:
            self.show_error('No hay conexion con el servidor')
        data = self.cliente.recv(1024)
        print(f'Recibido: {data}')

    @Slot()
    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'Zip Files(*.zip)')
        self.file = open(file_name[0], 'rb')
        self.ui.lineEditRuta.setText(file_name[0])

    @Slot()
    def send_file(self):
        try:
            data = 'iniciozip'
            bytes = data.encode()
            self.cliente.send(bytes)
        except:
            self.show_error('No hay conexion con el servidor')
        try:
            i = self.file.read(500)
        except:
            self.show_error('No se puede leer el archivo, intente abrirlo nuevamente')
        while i:
            self.cliente.send(i)
            i = self.file.read(500)
        time.sleep(0.1)
        data = 'finzip'
        bytes = data.encode()
        self.cliente.send(bytes)
        print('Se envio el archivo')
        self.file.close()
