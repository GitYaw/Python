import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

window.show()
sys.exit(app.exec())