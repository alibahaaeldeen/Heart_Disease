# write here a code for the main app and the first screen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,QLabel,
    QPushButton,QVBoxLayout
)
from instr import*
from second_win import *


class MainWin(QWidget):
    def __init__ (self):
        super(). __init__ ()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.layout=QVBoxLayout()

        #LABELS          
        self.hello_label =QLabel(txt_hello)
        self.inst_label =QLabel(txt_instruction)

        #button...
        self.btn = QPushButton(txt_next)
        self.layout.addWidget(self.hello_label,alignment=Qt.AlignLeft)
        self.layout.addWidget(self.inst_label,alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn,alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def next_win(self):
        self.tw = Testwin()
        self.hide()

    def connects(self):
        self.btn.clicked.connect(self.next_win)



app = QApplication([])
Win= MainWin()
app.exec_()