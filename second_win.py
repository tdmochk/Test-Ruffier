import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
import final_win

#win_x, win_y = 200, 100
#win_width, win_height = 1000, 600
 
#txt_title = ''
#txt_name = ''
#txt_hintname = "Введите имя"
#txt_hintage = "Введите возраст"
#txt_test1 = 'obama'
#txt_test2 = 'obunga'
#txt_test3 = 'suspicious'
#txt_sendresults = 'Отправить результаты'
#txt_hinttest1 = '0'
#txt_hinttest2 = '0'
#txt_hinttest3 = '0'
#txt_starttest1 = ''
#txt_starttest2 = ''
#txt_starttest3 = ''
#txt_age = ''
#txt_finalwin = ''
#txt_index = ''
#txt_workheart = ''

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
        self.button1 = QPushButton(txt_starttest1)
        self.pole3 = QLineEdit('0')
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.pole4 = QLineEdit('0')
        self.pole5 = QLineEdit('0')
        self.button4 = QPushButton(txt_sendresults)
        self.timer = QLabel('00:00:15')
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
        self.r_line.addWidget(self.timer, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.button4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = final_win()
run = QApplication([])
TestWin = TestWin()
TestWin.show()
run.exec_()
smh1 = TestWin(self.pole1)