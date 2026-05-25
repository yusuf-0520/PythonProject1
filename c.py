class School:
    def __init__(self):
        self.my_school = {
            "yusuf opemipo": 60,
            "adekeye oluwaseyi": 83,
            "bisola habibat": 45,
            "daniel james": 59,
            "adeola mercy": 52,
            "ade damilola": 34,
            "aderiwa tomiwa": 27,
            "boluwatife ikmat": 72
        }
        self.grade = ["A", "B", "C", "D", "E", "F"]

    def check_grade(self):
        is_running = True
        while is_running:
            name = input("Enter your name: ").lower()
            if name in self.my_school:
                value = self.my_school[name]
                if value >= 70:
                    print(f"{name}:your score is {value} ({self.grade[0]})")
                elif value >= 60:
                    print(f"{name}:your score is {value} {self.grade[1]}")
                elif value >= 50:
                    print(f"{name}:your score is {value} {self.grade[2]}")
                elif value >= 45:
                    print(f"{name}:your score is {value} {self.grade[3]}")
                elif value >= 40:
                    print(f"{name}:your score is {value} {self.grade[4]}")
                else:
                    print(f"{name}: {self.grade[5]}")
            elif name == "q":
                print("you've exited the program")
                is_running = False
            else:
                print(f"{name} is not found")




school = School()
school.check_grade()

self.setWindowTitle("My Calculator App")
vbox = QVBoxLayout()
vbox.addWidget(self.line_edit)

self.setLayout(vbox)
self.line_edit.setAlignment(Qt.AlignHCenter)


hbox2 = QHBoxLayout()
hbox2.addWidget(self.button6)
hbox2.addWidget(self.button7)
hbox2.addWidget(self.button8)
hbox3 = QHBoxLayout()
hbox3.addWidget(self.button10)
hbox3.addWidget(self.button11)
hbox3.addWidget(self.button12)
hbox4 = QHBoxLayout()
hbox4.addWidget(self.button14)
hbox4.addWidget(self.button15)
hbox4.addWidget(self.button16)
hbox5 = QHBoxLayout()
hbox5.addWidget(self.button1)
hbox5.addWidget(self.button5)
hbox5.addWidget(self.button9)
hbox5.addWidget(self.button13)
self.setLayout(vbox)
self.setStyleSheet(""""
    QPushButton, QLineEdit{
        font-size: 50px;




""")