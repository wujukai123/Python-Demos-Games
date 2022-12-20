from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 51, 16))
        self.label_2.setObjectName("label_2")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置文本框为密码
        self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000,99999999))  # 设置只能输入8位数字
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 61, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico")))  # 为“登录”按钮设置图标


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 51, 16))
        self.label_2.setObjectName("label_2")


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 90, 71, 18))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)  # 设置“管理员单选按钮默认选中


        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 90, 81, 18))
        self.radioButton_2.setObjectName("radioButton_2")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 120, 61, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QIcon(QPixmap("exit.ico")))  # 为“退出”按钮设置图标


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


        self.pushButton.clicked.connect(self.login)  # 为“登录”按钮的clicked信号绑定自定义槽函数
        self.pushButton_2.clicked.connect(MainWindow.close)  # 为“退出”按钮的clicked信号绑定MainWindow窗口自带的close(）槽函数
        self.radioButton.toggled.connect(self.select)  # 为单选按钮的toggled信号绑定自定义槽函数




        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def login(self):
        from PyQt5.QtWidgets import QMessageBox
        # 使用information()方法弹出信息提示框
        QMessageBox.information(MainWindow, "登录信息", "用户名: " + self.lineEdit.text() +
                                "  密码:" + self.lineEdit_2.text(), QMessageBox.Ok)


    # 自定义槽函数，用来判断用户登录身份
    def select(self):
        if self.radioButton.isChecked():    # 判断是否为管理员登录
            QMessageBox.information(MainWindow, "提示", "您选择的是 管理员 登录", QMessageBox.Ok)
        elif self.radioButton_2.isChecked():    # 判断是否为普通用户登录
            QMessageBox.information(MainWindow, "提示", "您选择的是 普通用户  登录", QMessageBox.Ok)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密 码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "普通用户"))


import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
