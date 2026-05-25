import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("del", self)
        self.button2 = QPushButton("8", self)
        self.button3 = QPushButton("%", self)
        self.button4 = QPushButton("/", self)
        self.button5 = QPushButton("7", self)
        self.button6 = QPushButton("5", self)
        self.button7 = QPushButton("9", self)
        self.button8 = QPushButton("*", self)
        self.button9 = QPushButton("4", self)
        self.button10 = QPushButton("2", self)
        self.button11 = QPushButton("6", self)
        self.button12 = QPushButton("-", self)
        self.button13 = QPushButton("1", self)
        self.button14 = QPushButton("0", self)
        self.button15= QPushButton("3", self)
        self.button16 = QPushButton("+", self)
        self.button17 = QPushButton("=", self)
        self.line_edit = QLineEdit()
        self.init_ui()


    def init_ui(self):

        self.setWindowTitle("ope calculator app")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.button1)
        hbox1.addWidget(self.button2)
        hbox1.addWidget(self.button3)
        hbox1.addWidget(self.button4)

        hbox2 = QHBoxLayout()

        hbox2.addWidget(self.button5)
        hbox2.addWidget(self.button6)
        hbox2.addWidget(self.button7)
        hbox2.addWidget(self.button8)

        hbox3 = QHBoxLayout()

        hbox3.addWidget(self.button9)
        hbox3.addWidget(self.button10)
        hbox3.addWidget(self.button11)
        hbox3.addWidget(self.button12)

        hbox4 = QHBoxLayout()

        hbox4.addWidget(self.button13)
        hbox4.addWidget(self.button14)
        hbox4.addWidget(self.button15)
        hbox4.addWidget(self.button16)

        hbox5 = QHBoxLayout()
        hbox5.addStretch()

        hbox5.addWidget(self.button17)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setStyleSheet("""
            QPushButton{
                
                font-size: 30px;
                font-weight: bold;
                font-family: calibri;
                border-raduis: 50px;
                border-color: black;
                
            }
            QLineEdit{
                padding: 20px;
                font-size: 30px;
                font-weight: bold;
                font-family: calibri;
            }
            
        """)
        central_widget.setLayout(vbox)
        self.line_edit.show()

        self.button2.clicked.connect(self.button_clicked)
        self.button5.clicked.connect(self.button_clicked)
        self.button6.clicked.connect(self.button_clicked)
        self.button7.clicked.connect(self.button_clicked)
        self.button9.clicked.connect(self.button_clicked)
        self.button10.clicked.connect(self.button_clicked)
        self.button11.clicked.connect(self.button_clicked)
        self.button13.clicked.connect(self.button_clicked)
        self.button14.clicked.connect(self.button_clicked)
        self.button15.clicked.connect(self.button_clicked)
        self.button4.clicked.connect(self.operator_clicked)
        self.button8.clicked.connect(self.operator_clicked)
        self.button12.clicked.connect(self.operator_clicked)
        self.button16.clicked.connect(self.operator_clicked)
        self.button3.clicked.connect(self.operator_clicked)
        self.button17.clicked.connect(self.solve)
        self.button1.clicked.connect(self.delete)
    def button_clicked(self):

        button = self.sender()
        self.line_edit.setText(self.line_edit.text() + button.text())

    def operator_clicked(self):
        button = self.sender()
        self.line_edit.setText(self.line_edit.text() + button.text())


    def solve(self):
        button = self.sender()
        if button.text() == "=":
            result = eval(self.line_edit.text())
            self.line_edit.setText(str(result))
        else:
            self.line_edit.setText(self.line_edit.text() + button.text())

    def delete(self):
        button = self.sender()
        if button.text() == "del":
            current = self.line_edit.text()
            self.line_edit.setText(current[:-1])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())