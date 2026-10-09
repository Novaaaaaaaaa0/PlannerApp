import sys
import json
import PySide6.QtCore
import PySide6.QtWidgets

class MainWindow(PySide6.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		# self.button_is_checked = True

		self.setWindowTitle("My App")

		# self.button = PySide6.QtWidgets.QPushButton(":3")
		self.te = PySide6.QtWidgets.QTextEdit(self)
		# self.button.setCheckable(True)
		# self.button.clicked.connect(self.the_button_was_released)
		# self.button.setChecked(self.button_is_checked)

		self.setCentralWidget(self.te)

		self.available_geometry = self.te.screen().availableGeometry()
		self.te.resize((self.available_geometry.width() * 2) / 3, (self.available_geometry.height() * 2) / 3)
		self.te.move((self.available_geometry.width() - self.te.width())/2, (self.available_geometry.height() - self.te.height())/2)
		
		self.f = open("data/test.json")

	'''def the_button_was_released(self):
			self.button_is_checked = self.button.isChecked()
			print(self.button_is_checked)'''

app = PySide6.QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()