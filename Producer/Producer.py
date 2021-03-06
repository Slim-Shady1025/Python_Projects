import sys
import datetime

from PublicFunctions.GetDBConn import ConnDB
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox

from ProducerInfoUI import Ui_MainWindow
import VacOrderUI as u2
import VacProSearchUI as u3
import VacProduceUI as u4
import pymysql


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
        self.label.setGeometry(QtCore.QRect(60, 0, 552, 146))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 150, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 60, 43))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 196, 60, 43))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 200, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 240, 93, 41))
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

        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????????????"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Photo"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.label.setPixmap(QtGui.QPixmap("images/top.png"))
        self.label.setStyleSheet("{border-radius:20px;}")
        self.label_2.setPixmap(QtGui.QPixmap("images/UserName.png"))
        self.label_3.setPixmap(QtGui.QPixmap("images/Password.png"))

    def Sing(self):

        User = self.lineEdit.text()
        PasswordText = self.lineEdit_2.text()
        if len(PasswordText) < 10:
            QMessageBox.information(None, 'Error', '        ???????????????10???     ')
            return

        try:
            file = open('Admin/CaacUser' + User + '.txt', 'r')
        except Exception as e:
            QMessageBox.information(None, '????????????', '     ???????????????       ')
            return

        file.seek(6)
        MessageName = file.readline()
        Password = file.readline()
        Password = Password[10:]

        Judege = (User in MessageName)
        if Judege:
            Judege = (PasswordText in Password)
            if Judege:
                QMessageBox.information(None, '????????????', '     ????????????        ')
                win0.close()
                win.show()
            else:
                QMessageBox.information(None, '????????????', '       ??????????????????      ')
            return
        else:
            QMessageBox.information(None, '????????????', '     ???????????????       ')
            return


class SecondWindow(QMainWindow):
    def slot1(self):
        win2.close()

    def __init__(self, parent = None):
        super(SecondWindow, self).__init__(parent)
        self.ui = u2.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.GetVaccineOrder)

    def GetVaccineOrder(self):
        # ???????????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:???????????????ID
        # ProducerNo = input('???????????????ID:')
        ProducerNo = self.ui.lineEdit.text()
        GetLicenseSql = "SELECT HospitalNo,VaccineName,OrderAmount,OrderTime FROM `VaccineOrder` WHERE ProducerNo = %s"
        cursor.execute(GetLicenseSql, ProducerNo)
        VaccineOrder = cursor.fetchall()
        if VaccineOrder:
            print(VaccineOrder)
            # TODO:????????????????????????
            x = 0
            for i in VaccineOrder:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccineOrder[x][y])))
                    y = y + 1
                x = x + 1
            cursor.close()
            conn.close()
        else:
            # TODO:??????MessageBox??????ID?????????
            # return False
            QMessageBox.information(self, '??????', '???ID????????????', QMessageBox.Close)
            pass


class ThirdWindow(QMainWindow):
    def slot1(self):
        win3.close()

    def __init__(self, parent = None):
        super(ThirdWindow, self).__init__(parent)
        self.ui = u3.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.GetProduceData)

    def GetProduceData(self):
        # ??????????????????
        ProducerID = self.ui.lineEdit.text()
        conn = ConnDB()
        cursor = conn.cursor()
        GetProduceDataSql = "SELECT * FROM `Produce` WHERE ProducerNo=%s"
        cursor.execute(GetProduceDataSql, ProducerID)
        VaccineOrder = cursor.fetchall()
        if VaccineOrder:
            print(VaccineOrder)
            x = 0
            for i in VaccineOrder:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccineOrder[x][y])))
                    y = y + 1
                x = x + 1
            # TODO:????????????????????????
            cursor.close()
            conn.close()
        else:
            # TODO:????????????MessageBox??????ID?????????
            QMessageBox.information(self, '??????', '???ID????????????', QMessageBox.Close)
            pass


class FourthWindow(QMainWindow):
    def slot1(self):
        win4.close()

    def __init__(self, parent = None):
        super(FourthWindow, self).__init__(parent)
        self.ui = u4.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.ProduceVaccine)

    def ProduceVaccine(self):
        # ??????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:?????????ID ??? ??????????????????????????????
        # ProducerNo = input('???????????????ID:')
        # VaccineName = input('??????????????????????????????:')
        ProducerNo = self.ui.lineEdit.text()
        VaccineName = self.ui.lineEdit_2.text()
        if ProducerNo == '' or VaccineName=='':
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
        cursor.execute("SELECT ProducerNo FROM `Producer`")
        AllProducer=cursor.fetchall()
        if (ProducerNo,) not in AllProducer:
            QMessageBox.information(self, '??????', '??????ID', QMessageBox.Close)
            return
        print(ProducerNo)
        print(VaccineName)
        GetLicenseDateSql = "SELECT LicenseDate FROM `ProducerLicense` WHERE ProducerNo = %s ORDER BY LicenseDate DESC LIMIT 1"
        cursor.execute(GetLicenseDateSql, ProducerNo)
        LicenseDate = cursor.fetchall()[0][0]
        [year, month, day] = str(LicenseDate).split('-')
        print(year + month + day)
        date = year + '-' + month + '-' + day
        PrduceAmount = self.ui.lineEdit_3.text()
        if PrduceAmount == '':
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
        ProduceAmount = int(self.ui.lineEdit_3.text())
        print(ProduceAmount)
        if datetime.datetime.today() > datetime.datetime.strptime(date, "%Y-%m-%d"):
            # TODO:????????????MessageBox??????
            print('?????????????????????')
            # return False
            QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Close)
        else:
            # ProduceAmount = int(self.ui.lineEdit_3.text())
            # print(ProduceAmount)
            ProduceSql = "INSERT INTO `Produce` VALUES (%s,%s,%s,%s)"
            cursor.executemany(ProduceSql, [(ProducerNo, VaccineName, ProduceAmount, datetime.datetime.now())])
            conn.commit()

            VaccineNotmp = 'V' + ProducerNo[1:3] + str(datetime.datetime.now().year)
            cursor.execute("SELECT VaccineNo FROM `Vaccine` WHERE ProducerNo=%s ORDER BY VaccineNo desc limit 1",
                           ProducerNo)
            LastVaccine = cursor.fetchall()
            if LastVaccine:
                LastVaccineNo = LastVaccine[0][0][7:]
            else:
                LastVaccineNo = '001'
            print(LastVaccineNo)

            NowVaccineNo = VaccineNotmp + LastVaccineNo
            print(NowVaccineNo)
            # ???????????? ????????????Vaccine???
            for i in range(int(LastVaccineNo) + 1, ProduceAmount + int(LastVaccineNo) + 1):
                if i < 10:
                    NewVaccineNo = NowVaccineNo[0:7] + '00' + str(i)
                elif i < 100:
                    NewVaccineNo = NowVaccineNo[0:7] + '0' + str(i)
                else:
                    NewVaccineNo = NowVaccineNo[0:7] + str(i)
                ProductionDate = datetime.date.today()
                ExpirationDate = str(datetime.date.today().year + 1) + '-' + str(
                    datetime.date.today().month) + '-' + str(datetime.date.today().day)
                cursor.executemany("INSERT INTO `Vaccine` VALUES(%s,%s,'???',%s,%s,%s,NULL,NULL)",
                                   [(NewVaccineNo, VaccineName, ProducerNo, ProductionDate, ExpirationDate)])
                conn.commit()
            cursor.close()
            conn.close()
            # TODO:??????MessageBox??????????????????
            QMessageBox.information(self, '??????', '????????????', QMessageBox.Close)


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def slot1(self):
        win2.show()

    def slot2(self):
        win3.show()

    def slot3(self):
        win4.show()

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        # ??????????????????
        self.pushButton.clicked.connect(self.GetLicense)

    def GetLicense(self):
        # ?????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:???????????????ID
        ProducerNo = self.lineEdit.text()

        GetLicenseSql = "SELECT * FROM `ProducerLicense` WHERE ProducerNo = %s"
        cursor.execute(GetLicenseSql, ProducerNo)
        License = cursor.fetchall()
        if License:
            print(License)
            # TODO:????????????????????????
            x = 0
            for i in License:
                y = 0
                for j in i:
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(License[x][y])))
                    y = y + 1
                x = x + 1
            cursor.close()
            conn.close()
        else:
            # TODO:??????MessageBox??????ID?????????
            # return False
            QMessageBox.information(self, '??????', '???ID????????????', QMessageBox.Close)
            pass


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win0 = StartDesinger()
    win0.show()
    win = MyMainWindow()
    win2 = SecondWindow()
    win3 = ThirdWindow()
    win4 = FourthWindow()
    sys.exit(app.exec())
