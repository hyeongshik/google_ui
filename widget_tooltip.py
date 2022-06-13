import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget) :

    def  __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()

    def initWindow(self) :
        QToolTip.setFont(QFont("Arial",10))
        self.setToolTip("툴팁이 <u>노출</u>됩니다")  #위젯판에 툴팁 적용

        btn1=QPushButton("버튼1",self)
        btn1.setToolTip("버튼을 클릭하면 실행됩니다")  # 버튼에 툴팁 적용

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())








