import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from Dialog.HttpLogin import HttpPost

class Ui_dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi() #界面绘制交给InitUi方法

    def setupUi(self):
        self.setObjectName("学生登录界面")
        self.resize(535, 344)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)

        #注意变量定义的先后顺序
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        #将其设为密码输入框
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        #禁止窗口变化（最上方的设置）
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(100, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        #给取消按钮添加了响应事件
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)

        #确认按钮
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.forlogin)#带参数默认执行 不带参数点击执行

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 100, 72, 21))

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 155, 72, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "取消"))
        self.pushButton_2.setText(_translate("dialog", "确认"))
        self.label.setText(_translate("dialog", "账号："))
        self.label_2.setText(_translate("dialog", "密码："))



    def forlogin(self):
       #获取账号输入框的类容和密码输入框的类容
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        sign = HttpPost.login(name,password)
        if sign=="true":
            print("登录成功")
            self.QCoreApplication.instance().quit#关闭当前窗口
        else:
            print("登录失败")
            reply = QtWidgets.QMessageBox.question(self,"警告","密码错误请重新登录",QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.lineEdit_2.setText("")
                self.lineEdit.setText("")
            else:
                self.QCoreApplication.instance().quit#关闭当前窗口



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my=Ui_dialog()
    my.show()
    sys.exit(app.exec_())
