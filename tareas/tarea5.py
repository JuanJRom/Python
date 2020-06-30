from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import Slot
from Ui_MainWindow import Ui_MainWindow
from Modulos.StudentIO import student


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Tarea 5')
        self.error = QMessageBox()
        self.listStudents = []

        self.ui.add.clicked.connect(self.addF)
        self.ui.deleteS.clicked.connect(self.delete_student)
        self.ui.readS.clicked.connect(self.read_student)
        self.ui.listWidget.currentRowChanged.connect(self.show_details)

    def show_error(self, message):
        self.error.setText(message)
        self.error.setIcon(QMessageBox.Warning)
        self.error.exec_()

    @Slot()
    def addF(self):
        temp = student(self.ui.name.text(), self.ui.email.text(), self.ui.password.text())
        self.listStudents.append(temp)
        student.saveStudentP(self.listStudents)
        self.ui.listWidget.addItem(temp.getName())
        self.ui.name.setText('')
        self.ui.email.setText('')
        self.ui.password.setText('')

    @Slot()
    def show_details(self):
        self.ui.textEdit.clear()
        temp = self.listStudents[self.ui.listWidget.currentRow()]
        self.ui.textEdit.append(str(temp))

    @Slot()
    def delete_student(self):
        try:
            self.listStudents.pop(self.ui.listWidget.currentRow())
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        except:
            self.show_error("No hay estudiantes por borrar")

    @Slot()
    def read_student(self):
        self.listStudents.append(student.readStudentP('studentsP.db'))
        for i in student.readStudentP('studentsP.db'):
            self.ui.textEdit.append(str(i))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()

    app.exec_()
