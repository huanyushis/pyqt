# QMainWindow ：可以包含菜单栏、工具栏、状态栏、标题栏，是常见的窗口形式
# QDialog ：是对话窗口的基类，没有菜单栏、工具栏、状态栏
# QWiget ：不确定窗口的用途，就使用QWiget

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QPushButton,QHBoxLayout,QWidget
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__()

        self.setWindowTitle("第一个主窗口应用")
        self.resize(640,480)
        self.status = self.statusBar()
        self.status.showMessage("你好",5000)
        self.button = QPushButton()
        self.button.setText("你好")
        self.button.clicked.connect(self.onClick_button)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        # print(screen,size)
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    #单击事件的方法
    def onClick_button(self):
        sender = self.sender()
        print(sender.text()+'被点击了')
        app = QApplication.instance()
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\admin\Desktop\webstorm.ico'))

    main=FirstMainWin()
    main.center()
    main.show()
    sys.exit(app.exec())
