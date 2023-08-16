import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
	"logo": [],
	"button": [],
	"score": [],
	"question": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.move(200, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

def frame1():
	# display logo
	image = QPixmap("logo.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 100px;")
	widgets["logo"].append(logo)

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
	widgets["button"].append(button)

	grid.addWidget(logo, 0, 0)
	grid.addWidget(button, 1, 0)

def frame2():
	score = QLabel("80")
	score.setAlignment(QtCore.Qt.AlignRight)
	score.setStyleSheet(
		"font-size: 35px; " +
		"color: 'white'; " +
		"padding: 25px 20px 0px 20px; " +
		"margin: 20px 200px; " +
		"background: '#64A314'; " +
		"border: 1px solid '#64A314'; " +
		"border-radius: 45px;"
	)
	widgets["score"].append(score)
	
	question = QLabel("Placeholder for text of the trivia question")
	question.setAlignment(QtCore.Qt.AlignCenter)
	question.setWordWrap(True)
	question.setStyleSheet(
		"font-family: Shanti; " +
		"font-size: 25px; " +
		"color: 'white'; " +
		"padding: 75px; "
	)
	widgets["question"].append(question)

	grid.addWidget(score, 0, 1)
	grid.addWidget(question, 1, 0, 1, 2)
	
frame2()

window.setLayout(grid)

window.show()
sys.exit(app.exec())