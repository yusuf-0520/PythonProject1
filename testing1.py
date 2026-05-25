import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
QLineEdit, QComboBox, QPushButton, QVBoxLayout, QWidget)

class JobMatcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle("Student Job Matcher")
        self.setMinimumSize(400, 300)

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Name input
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        layout.addWidget(QLabel("Full Name:"))
        layout.addWidget(self.name_input)

app = QApplication(sys.argv)
window = JobMatcher()
window.show()
sys.exit(app.exec_())