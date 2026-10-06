import sys
import json
import PySide6.QtCore
import PySide6.QtWidgets

class MainWindow(PySide6.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.button_is_checked = True

		self.setWindowTitle("My App")

		self.button = PySide6.QtWidgets.QPushButton(":3")
		self.button.setCheckable(True)
		self.button.clicked.connect(self.the_button_was_released)
		self.button.setChecked(self.button_is_checked)

		self.setFixedSize(PySide6.QtCore.QSize(400,300))
		self.setCentralWidget(self.button)

	def the_button_was_released(self):
			self.button_is_checked = self.button.isChecked()
			print(self.button_is_checked)

app = PySide6.QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()