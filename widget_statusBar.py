import sys
from PyQt5.QtGui  import QIcon
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow) :

    def __init__(self) :
        super().__init__()  # 부모클래스의 초기화자 호출
        self.initWindow()

    def initWindow(self):
        self.statusBar().showMessage('ver 1.0.4')  #상태표시줄 메인윈도우에 붙이기
        exitWindow = QAction(QIcon('icons/2.png'), 'EXIT', self)
        exitWindow.setShortcut('CTRL+Q')
        exitWindow.setStatusTip('프로그램 종료')
        exitWindow.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        filemenu=menubar.addMenu('&파일')
        filemenu.addAction(exitWindow)

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
