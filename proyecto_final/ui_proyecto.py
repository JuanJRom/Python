# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_proyecto(object):
    def setupUi(self, proyecto):
        if not proyecto.objectName():
            proyecto.setObjectName(u"proyecto")
        proyecto.resize(410, 481)
        self.centralwidget = QWidget(proyecto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 391, 111))
        self.pushButtonConect = QPushButton(self.groupBox)
        self.pushButtonConect.setObjectName(u"pushButtonConect")
        self.pushButtonConect.setGeometry(QRect(20, 60, 361, 31))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 371, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditIP = QLineEdit(self.layoutWidget)
        self.lineEditIP.setObjectName(u"lineEditIP")

        self.horizontalLayout.addWidget(self.lineEditIP)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEditPort = QLineEdit(self.layoutWidget)
        self.lineEditPort.setObjectName(u"lineEditPort")

        self.horizontalLayout.addWidget(self.lineEditPort)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 391, 161))
        self.pushButtonSendEstudent = QPushButton(self.groupBox_2)
        self.pushButtonSendEstudent.setObjectName(u"pushButtonSendEstudent")
        self.pushButtonSendEstudent.setGeometry(QRect(20, 120, 351, 31))
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 361, 80))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEditName = QLineEdit(self.layoutWidget1)
        self.lineEditName.setObjectName(u"lineEditName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditName)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEditEmail = QLineEdit(self.layoutWidget1)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditEmail)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEditPassword = QLineEdit(self.layoutWidget1)
        self.lineEditPassword.setObjectName(u"lineEditPassword")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditPassword)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 300, 391, 111))
        self.pushButtonSendFile = QPushButton(self.groupBox_3)
        self.pushButtonSendFile.setObjectName(u"pushButtonSendFile")
        self.pushButtonSendFile.setGeometry(QRect(20, 70, 351, 31))
        self.layoutWidget2 = QWidget(self.groupBox_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 40, 361, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSearsFile = QPushButton(self.layoutWidget2)
        self.pushButtonSearsFile.setObjectName(u"pushButtonSearsFile")

        self.horizontalLayout_2.addWidget(self.pushButtonSearsFile)

        self.lineEditRuta = QLineEdit(self.layoutWidget2)
        self.lineEditRuta.setObjectName(u"lineEditRuta")

        self.horizontalLayout_2.addWidget(self.lineEditRuta)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(280, 420, 121, 21))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        proyecto.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(proyecto)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 410, 20))
        proyecto.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(proyecto)
        self.statusbar.setObjectName(u"statusbar")
        proyecto.setStatusBar(self.statusbar)

        self.retranslateUi(proyecto)

        QMetaObject.connectSlotsByName(proyecto)
    # setupUi

    def retranslateUi(self, proyecto):
        proyecto.setWindowTitle(QCoreApplication.translate("proyecto", u"proyecto", None))
        self.groupBox.setTitle(QCoreApplication.translate("proyecto", u"Servidor", None))
        self.pushButtonConect.setText(QCoreApplication.translate("proyecto", u"Conectar", None))
        self.label.setText(QCoreApplication.translate("proyecto", u"IP:", None))
        self.label_2.setText(QCoreApplication.translate("proyecto", u"Puerto", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("proyecto", u"Estudiante", None))
        self.pushButtonSendEstudent.setText(QCoreApplication.translate("proyecto", u"Enviar", None))
        self.label_3.setText(QCoreApplication.translate("proyecto", u"Nombre:", None))
        self.label_4.setText(QCoreApplication.translate("proyecto", u"Correo:", None))
        self.label_5.setText(QCoreApplication.translate("proyecto", u"Contrase\u00f1a:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("proyecto", u"Archivo", None))
        self.pushButtonSendFile.setText(QCoreApplication.translate("proyecto", u"Enviar", None))
        self.pushButtonSearsFile.setText(QCoreApplication.translate("proyecto", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("proyecto", u"Estado:", None))
        self.label_7.setText(QCoreApplication.translate("proyecto", u"TextLabel", None))
    # retranslateUi

