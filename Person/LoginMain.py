# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Person import MyMainWindow


class StartDesinger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 450, 100))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 120, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 170, 31, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 170, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 210, 93, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.Sing)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Photo"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setPixmap(QtGui.QPixmap("images/top.png"))
        self.label.setStyleSheet("{border-radius:20px;}")
        self.label_2.setPixmap(QtGui.QPixmap("images/UserName.png"))
        self.label_3.setPixmap(QtGui.QPixmap("images/Password.png"))

    def Sing(self):

        User = self.lineEdit.text()

        PasswordText = self.lineEdit_2.text()
        if len(PasswordText) < 6:
            QMessageBox.information(None, 'Error', '         密码必须为六位         ')
            return

        file = open('Admin/CaacUser' + User + '.txt', 'r')
        file.seek(6)
        MessageName = file.readline()
        Password = file.readline()
        Password = Password[10:]

        Judege = (User in MessageName)
        if Judege:
            Judege = (PasswordText in Password)
            if Judege:
                QMessageBox.information(None, 'Pass', '         密码正确          ')
                main_win = MyMainWindow()
                main_win.show()
            else:
                QMessageBox.information(None, '错误', '          密码输入错误       ')
            return
        else:
            QMessageBox.information(None, 'Pass', '               查无此用户    ')
            return


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    StartLogin = StartDesinger()
    StartLogin.show()
    sys.exit(app.exec_())