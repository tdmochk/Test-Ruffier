import PyQt5
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
#from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
        self.show()
    def initUI(self):
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_hintname = QLabel(txt_hintname)
        self.txt_hintage = QLabel(txt_hintage)
        self.pole1 = QLineEdit(txt_name)
        self.pole2 = QLineEdit('0')
        self.button1 = QPushButton(txt_starttest1)  #кнопка 1 тест
        self.pole3 = QLineEdit('0')
        self.button2 = QPushButton(txt_starttest2)  #кнопка 2 тест
        self.button3 = QPushButton(txt_starttest3)  #кнопка 3 тест
        self.pole4 = QLineEdit('0')
        self.pole5 = QLineEdit('0')
        self.button4 = QPushButton(txt_sendresults)
        self.text_timer = QLabel('00:00:00')   ###
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_hintname, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pole1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hintage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pole2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pole3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pole4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.pole5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button4, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight) ###
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    def next_click(self):
        self.hide()
        self.fw = final_win()
    def timer_test(self):                                        #таймер 1
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        #self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):                                        #таймер 2
        global time
        time = QTime(0, 0, 31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        #self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):                                        #таймер 3
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)

        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

        self.text_timer.setText(time.toString("hh:mm:ss"))
        #self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


run = QApplication([])
TestWin = TestWin()
TestWin.show()
run.exec_()
smh1 = TestWin(self.pole1)