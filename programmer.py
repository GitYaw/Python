import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.move(200, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

# display logo
image = QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet("margin-top: 100px;")

# button widget
button = QPushButton("PLAY")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
	"*{border: 4px solid '#BC006C'; " +
	"border-radius: 45px; " +
	"font-size: 35px; " +
	"color: 'white'; " +
	"padding: 25px 0px; " +
	"margin: 100px 200px;} " +
	"*:hover{background: '#BC006C';}"
)

grid.addWidget(logo, 0, 0)
grid.addWidget(button, 1, 0)


window.setLayout(grid)

window.show()
sys.exit(app.exec())