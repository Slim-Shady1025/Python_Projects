# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VacProduceUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 120, 151, 71))
        self.pushButton_5.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 161, 41))
        self.label.setStyleSheet("font: 14pt \"Algerian\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 270, 301, 71))
        self.pushButton.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 60, 251, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 181, 31))
        self.label_2.setStyleSheet("font: 14pt \"Algerian\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 130, 251, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 151, 21))
        self.label_3.setStyleSheet("font: 14pt \"Algerian\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 190, 251, 41))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 270, 151, 61))
        self.pushButton_6.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(self.lineEdit.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.lineEdit_2.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.lineEdit_3.clear) # type: ignore
        self.pushButton_6.clicked.connect(MainWindow.slot1) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进行疫苗生产"))
        self.pushButton_5.setText(_translate("MainWindow", "刷新"))
        self.label.setText(_translate("MainWindow", "请输入厂商ID"))
        self.pushButton.setText(_translate("MainWindow", "进行疫苗生产"))
        self.label_2.setText(_translate("MainWindow", "请输入疫苗名称"))
        self.label_3.setText(_translate("MainWindow", "请输入产量"))
        self.pushButton_6.setText(_translate("MainWindow", "返回"))
