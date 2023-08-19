import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
	"logo": [],
	"button": [],
	"score": [],
	"question": [],
	"answer1": [],
	"answer2": [],
	"answer3": [],
	"answer4": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.move(200, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

def clearWidgets():
	for widget in widgets:
		if widgets[widget] != []:
			widgets[widget][-1].hide()
		for i in range(0, len(widgets[widget])):
			widgets[widget].pop()

def showStart():
	clearWidgets()
	frame1()

def startGame():
	clearWidgets()
	frame2()

def answerButton(answer, left, right):
	button = QPushButton(answer)
	button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
	button.setFixedWidth(485)
	button.setStyleSheet(
		"*{border: 4px solid '#BC006C'; " +
		"margin-left: " + str(left) + "px; " + 
		"margin-right: " + str(right) + "px; " + 
		"color: white; " +
		"font-family: 'shanti'; " +
		"font-size: 16px; " +
		"border-radius: 25px; " +
		"padding: 15px 0px; " +
		"margin-top: 20px;} " +
		"*:hover{background: '#BC006C';}"
	)
	button.clicked.connect(showStart)
	return button

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
	button.clicked.connect(startGame)
	widgets["button"].append(button)

	grid.addWidget(logo, 0, 0, 1, 2)
	grid.addWidget(button, 1, 0, 1, 2)

def frame2():
	score = QLabel("80")
	score.setAlignment(QtCore.Qt.AlignRight)
	score.setStyleSheet(
		"font-size: 35px; " +
		"color: 'white'; " +
		"padding: 15px 10px; " +
		"margin: 20px 200px; " +
		"background: '#64A314'; " +
		"border: 1px solid '#64A314'; " +
		"border-radius: 35px;"
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

	button1 = answerButton("answer1", 85, 5)
	button2 = answerButton("answer2", 5, 85)
	button3 = answerButton("answer3", 85, 5)
	button4 = answerButton("answer4", 5, 85)

	widgets["answer1"].append(button1)
	widgets["answer2"].append(button2)
	widgets["answer3"].append(button3)
	widgets["answer4"].append(button4)

	image = QPixmap("logo_bottom.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
	widgets["logo"].append(logo)
	
	grid.addWidget(score, 0, 1)
	grid.addWidget(question, 1, 0, 1, 2)
	grid.addWidget(button1, 2, 0,)
	grid.addWidget(button2, 2, 1)
	grid.addWidget(button3, 3, 0)
	grid.addWidget(button4, 3, 1)
	grid.addWidget(logo, 4, 0, 1, 2)
	
frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())