from PyQt5.QtWidgets import QApplication, QWidget, QPushButton ,QDesktopWidget ,QLabel ,QGridLayout
 
import webbrowser ,sys
 
 
class Ui_MainWindow(QWidget):
    item_name = "Smillet浏览器 1.0"
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.tips_1 = QLabel("网站：<a href='http://www.baidu.com/'>http://www.baidu.com/</a>");
        self.tips_1.setOpenExternalLinks(True)
 
        self.btn_webbrowser = QPushButton('在单独的窗口中打开网页', self)
 
        self.btn_webbrowser.clicked.connect(self.btn_webbrowser_Clicked)
 
        grid = QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(self.btn_webbrowser, 1, 0)
        grid.addWidget(self.tips_1, 2, 0)
 
        self.setLayout(grid)
 
        self.resize(250, 150)
        self.setMinimumSize(266, 304);
        self.setMaximumSize(266, 304);
        self.center()
        self.setWindowTitle(self.item_name)
        self.show()
 
 
    def btn_webbrowser_Clicked(self):
        webbrowser.open('http://www.baidu.com/')
 
 
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Ui_MainWindow()
    sys.exit(app.exec_())
