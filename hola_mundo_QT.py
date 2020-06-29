from PySide2.QtWidgets import QApplication, QLabel
import sys

app = QApplication([])
label = QLabel('Hola Mundo!')
label.show()
app.exec_()

