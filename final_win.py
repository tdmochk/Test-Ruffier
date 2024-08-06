import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self,pole2,pole3,pole4,pole5):
        super().__init__()
        self.pole2 = int(pole2)
        self.pole3 = pole3
        self.pole4 = pole4
        self.pole5 = pole5
        self.result = self.results()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
        self.show()
    def initUI(self):
        self.v_line = QVBoxLayout()
        self.setLayout(self.v_line)
        self.txt_workheart = QLabel(txt_workheart + self.result)
        self.workheart = QLabel(self.result)
        if self.result == txt_res6:
            self.v_line.addWidget(self.workheart, alignment = Qt.AlignCenter)
        else:
            self.v_line.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
    def connects(self):
        pass
    def results(self):
        self.index = (4*(int(self.pole3)+int(self.pole4)+int(self.pole5))-200)/10
        print(self.index)
        if self.pole2 >=15:                                 #15+
            if self.index >=15:
                return txt_res1
            elif self.index <15 and self.index>=11:
                return txt_res2
            elif self.index <11 and self.index >=6:
                return txt_res3
            elif self.index <6 and self.index >=0.5:
                return txt_res4
            else:
                return txt_res5

        elif self.pole2 >=13 and self.exp.age <=14:         #13-14
            if self.index >=16.5:
                return txt_res1
            elif self.index <16.5 and self.index>=12.5:
                return txt_res2
            elif self.index <12.5 and self.index >=7.5:
                return txt_res3
            elif self.index <7.5 and self.index >=2:
                return txt_res4
            else:
                return txt_res5

        elif self.pole2 >=11 and self.exp.age <=12:         #11-12
            if self.index >=18:
                return txt_res1
            elif self.index <18 and self.index>=14:
                return txt_res2
            elif self.index <14 and self.index >=9:
                return txt_res3
            elif self.index <9 and self.index >=3.5:
                return txt_res4
            else:
                return txt_res5

        elif self.pole2 >=9 and self.exp.age <=10:          #9-10
            if self.index >=19.5:
                return txt_res1
            elif self.index <19.5 and self.index>=15.5:
                return txt_res2
            elif self.index <15.5 and self.index >10.5:
                return txt_res3
            elif self.index <10.5 and self.index >=5:
                return txt_res4
            else:
                return txt_res5

        elif self.pole2 >=7 and self.exp.age <=8:           #7-8
            if self.index >=21:
                return txt_res1
            elif self.index <21 and self.index>=17:
                return txt_res2
            elif self.index <17 and self.index >=12:
                return txt_res3
            elif self.index <12 and self.index >=6.5:
                return txt_res4
            else:
                return txt_res5

        else:
            return txt_res6