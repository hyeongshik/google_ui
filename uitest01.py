import sys
from PyQt5.QtWidgets import *

app =QApplication (sys.argv) # QApplication 객체 생성

label1 = QLabel("Hellow neull123 ~~~!!!")
label1.show()

Button01 = QPushButton("버튼")
Button01.show()


app.exec_()  # 이벤트 루프

