# GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget
# function imports
from functions import frame1, frame2, frame3, frame4, grid

# initialize GUI application
app = QApplication(sys.argv)

# window settings
window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.move(200, 20)
window.setStyleSheet("background: #161219;")

frame4()

window.setLayout(grid)

window.show()
sys.exit(app.exec())