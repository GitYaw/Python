from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
from urllib.request import urlopen # accessing url
import json # data in json format
import pandas as pd # handling data
import random

url = "https://opentdb.com/api.php?amount=50&category=18&difficulty=medium&type=multiple"
with urlopen(url) as webpage:
	data = json.loads(webpage.read().decode())
	df = pd.DataFrame(data["results"])

def preloadData():
	question = df["question"][0]
	correct = df["correct_answer"][0]
	wrong = df["incorrect_answers"][0]

	parameters["question"].append(question)
	parameters["correct"].append(correct)

	answers = wrong + [correct]
	random.shuffle(answers)

	for i in range(4):
		parameters["answer" + str(i + 1)].append(answers[i])

parameters = {
	"question": [],
	"answer1": [],
	"answer2": [],
	"answer3": [],
	"answer4": [],
	"correct": []
}

preloadData()
print(parameters)

# global dictionary of widgets
widgets = {
	"logo": [],
	"button": [],
	"score": [],
	"question": [],
	"answer1": [],
	"answer2": [],
	"answer3": [],
	"answer4": [],
	"message": [],
	"message2": []
}

# initialize grid layout
grid = QGridLayout()

def clearWidgets():
	''' hide all existing widgets
		and remove from global dictionary '''
	for widget in widgets:
		if widgets[widget] != []:
			widgets[widget][-1].hide()
		for i in range(0, len(widgets[widget])):
			widgets[widget].pop()

def startGame():
	# start game, reset all widgets
	clearWidgets()
	frame2()

def answerButton(answer, left, right):
	# create answer button with custom left & right margins
	button = QPushButton(answer)
	button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
	button.setFixedWidth(485)
	button.setStyleSheet(
		# set variable margins
		"*{margin-left: " + str(left) + "px; " + 
		"margin-right: " + str(right) + "px; " + 
		'''
		border: 4px solid '#BC006C';
		border-radius: 25px;
		color: white;
		font-family: 'Shanti';
		font-size: 16px;
		margin-top: 20px;
		padding: 15px 0px;
		}
		*:hover{
			background: '#BC006C';
		}
		'''
	)
	return button

#****************************************
#				FRAME 1
#****************************************

def frame1():
	# logo widget
	image = QPixmap("logo.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 100px;")
	widgets["logo"].append(logo)

	# start button widget
	button = QPushButton("PLAY")
	button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
	button.setStyleSheet(
		'''
		*{
			border: 4px solid '#BC006C';
			border-radius: 45px;
			color: 'white';
			font-size: 35px;
			margin: 100px 200px;
			padding: 25px 0px;
		}
		*:hover{
			background: '#BC006C';
		}
		'''
	)
	# button callback
	button.clicked.connect(startGame)
	widgets["button"].append(button)

	# place widgets on grid
	grid.addWidget(logo, 0, 0, 1, 2)
	grid.addWidget(button, 1, 0, 1, 2)

#****************************************
#				FRAME 2
#****************************************

def frame2():
	# score widget
	score = QLabel("80")
	score.setAlignment(QtCore.Qt.AlignRight)
	score.setStyleSheet(
		'''
		background: '#64A314';
		border: 1px solid '#64A314';
		border-radius: 35px;
		color: 'white';
		font-size: 35px;
		padding: 15px 10px;
		margin: 20px 200px;
		'''
	)
	widgets["score"].append(score)
	
	# trivia question widget
	question = QLabel("Placeholder for the text of the trivia question")
	question.setAlignment(QtCore.Qt.AlignCenter)
	question.setWordWrap(True)
	question.setStyleSheet(
		'''
		color: 'white';
		font-family: 'Shanti';
		font-size: 25px;
		padding: 75px;
		'''
	)
	widgets["question"].append(question)

	# answer button widgets
	button1 = answerButton("answer1", 85, 5)
	button2 = answerButton("answer2", 5, 85)
	button3 = answerButton("answer3", 85, 5)
	button4 = answerButton("answer4", 5, 85)

	widgets["answer1"].append(button1)
	widgets["answer2"].append(button2)
	widgets["answer3"].append(button3)
	widgets["answer4"].append(button4)

	# footer logo widget
	image = QPixmap("logo_bottom.png")
	logo = QLabel()
	logo.setPixmap(image)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
	widgets["logo"].append(logo)
	
	# place widgets on grid
	grid.addWidget(score, 0, 1)
	grid.addWidget(question, 1, 0, 1, 2)
	grid.addWidget(button1, 2, 0,)
	grid.addWidget(button2, 2, 1)
	grid.addWidget(button3, 3, 0)
	grid.addWidget(button4, 3, 1)
	grid.addWidget(logo, 4, 0, 1, 2)

#****************************************
#				FRAME 3
#****************************************

def frame3():
	# retry widget
	message = QLabel("Sorry, your answer\nwas wrong. \nYour score is:")
	message.setAlignment(QtCore.Qt.AlignRight)
	message.setStyleSheet(
		'''
		color: 'white';
		font-family: 'Shanti';
		font-size: 35px;
		margin: 75px 5px;
		padding: 20px;
		'''
	)
	widgets["message"].append(message)

	# score widget
	score = QLabel("50")
	score.setStyleSheet(
		'''
		color: white;
		font-size: 100px;
		margin: 0 75px 0px 75px;
		'''
	)
	widgets["score"].append(score)

	# continue button widget
	button = QPushButton('TRY AGAIN')
	button.setStyleSheet(
		'''*{
			background:'#BC006C';
			border: 1px solid '#BC006C';
			border-radius: 40px;
			color: 'white';
			font-family: 'Arial';
			font-size: 25px;
			margin: 10px 300px;
			padding: 25px 0px;
		}
		*:hover{
			background:'#FF1B9E';
		}'''
	)
	button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
	widgets["button"].append(button)

	# footer logo widget
	pixmap = QPixmap('logo_bottom.png')
	logo = QLabel()
	logo.setPixmap(pixmap)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet(
		'''
		margin-bottom: 20px;
		margin-top: 75px;
		padding: 10px;
		'''
	)
	widgets["logo"].append(logo)

	# place widgets on grid
	grid.addWidget(message, 0, 0)
	grid.addWidget(score, 0, 1)
	grid.addWidget(button, 1, 0, 1, 2)
	grid.addWidget(logo, 2, 0, 1, 2)

#****************************************
#				FRAME 4
#****************************************

def frame4():
	# celebration widget
	message = QLabel("Congratulations! You\nare a true programmer!\nYour score is:")
	message.setAlignment(QtCore.Qt.AlignRight)
	message.setStyleSheet(
		'''
		color: 'white';
		font-family: 'Shanti';
		font-size: 25px;
		margin: 100px 0px;
		'''
	)
	widgets["message"].append(message)

	# score widget
	score = QLabel("100")
	score.setStyleSheet(
		'''
		color: #8FC740;
		font-size: 100px;
		margin: 0px 75px 0px 75px;
		'''
	)
	widgets["score"].append(score)

	# continue widget
	message2 = QLabel("Would you like to try again?")
	message2.setAlignment(QtCore.Qt.AlignCenter)
	message2.setStyleSheet(
		'''
		color: 'white';
		font-family: 'Shanti';
		font-size: 30px;
		margin-bottom: 75px;
		margin-top: 0px;
		'''
	)
	widgets["message2"].append(message2)

	# continue button widget
	button = QPushButton('Try Again')
	button.setStyleSheet(
		'''*{
			background:'#BC006C';
			color: 'white';
			border: 1px solid '#BC006C';
			border-radius: 40px;
			font-family: 'Shanti';
			font-size: 25px;
			margin: 10px 300px;
			padding: 25px 0px;
		}
		*:hover{
			background:'#FF1B9E';
		}'''
	)
	button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
	widgets["button"].append(button)

	# footer logo widget
	pixmap = QPixmap('logo_bottom.png')
	logo = QLabel()
	logo.setPixmap(pixmap)
	logo.setAlignment(QtCore.Qt.AlignCenter)
	logo.setStyleSheet(
		'''
		margin-bottom: 20px;
		margin-top: 75px;
		padding: 10px;
		'''
	)
	widgets["logo"].append(logo)

	# place widgets on grid
	grid.addWidget(message, 0, 0)
	grid.addWidget(score, 0, 1)
	grid.addWidget(message2, 1, 0, 1, 2)
	grid.addWidget(button, 2, 0, 1, 2)
	grid.addWidget(logo, 3, 0, 1, 2)