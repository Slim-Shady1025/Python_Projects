# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManVacOrdSearchUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 110, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 430, 171, 61))
        self.pushButton.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 430, 171, 61))
        self.pushButton_2.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(840, 280, 141, 61))
        self.pushButton_5.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 171, 21))
        self.label.setStyleSheet("font: 14pt \"Algerian\";")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 180, 681, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 40, 251, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 171, 21))
        self.label_2.setStyleSheet("font: 14pt \"Algerian\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(self.lineEdit.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.lineEdit_2.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.tableWidget.clearContents) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.slot1) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "查看疫苗交易订单"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.pushButton_5.setText(_translate("MainWindow", "刷新"))
        self.label.setText(_translate("MainWindow", "请输入医院ID"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2."))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3."))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4."))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5."))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6."))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7."))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8."))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9."))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "医院编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "生产商编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "疫苗名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "订购量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "订购日期"))
        self.label_2.setText(_translate("MainWindow", "请输入生产商ID"))