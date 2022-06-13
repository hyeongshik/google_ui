import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget) :

    def  __init__(self):
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()

    def initWindow(self) :

        label_red = QLabel('빨강')
        label_blue = QLabel('파랑')

        label_red.setStyleSheet(
            "color:red ;"
            "border-style:solid;"
            "border-width:2px ;"
            "border-color:red ;"
            "background-color:pink"
        )

        label_blue.setStyleSheet(
            "color:blue ;"
            "border-style:solid;"
            "border-width:2px ;"
            "border-color:blue ;"
            "background-color:gray"
        )

        styleBox = QVBoxLayout()
        styleBox.addWidget(label_red)
        styleBox.addWidget(label_blue)

        self.setLayout(styleBox)

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


