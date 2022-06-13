import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class  = uic.loadUiType("ui/mywin.ui")[0]

class MyWindow(QMainWindow, form_class) :
    def __init__(self):
        # super().__init__()  #부모클래스의 초기화자를 호출(안하면 에러)
        p = super()
        p.__init__()
        self.setupUi(self)

        self.setWindowTitle("Hello neull123 ~~ @@@")
        self.setWindowIcon(QIcon("icons/2.png"))

        # btn1 = QPushButton("Button1",self)
        # btn1.move(30,50)
        #btn2 = QPushButton("Button2", self)
        #btn2.move(200, 50)

        self.btn1.clicked.connect(self.btn1Click)   #시그널
        self.btn2.clicked.connect(self.btn2Click)

    def btn1Click(self):
        self.label1.setText("버튼 1 이 클릭됨")  # 슬롯 이글짜로 세팅이 다시 되는것이다.
        self.lineEdit1.setText("버튼 1 이 클릭됨 !!!!!")
        print("버튼1이 클릭됨")


    def btn2Click(self):
        self.label1.setText("버튼 2 이 클릭됨")  # 슬롯
        self.lineEdit1.setText("버튼 2 이 클릭됨 @@@@@!!!!!")
        print("버튼2이 클릭됨")

qApp = QApplication(sys.argv)

myWin = MyWindow()
myWin.show()

qApp.exec_()