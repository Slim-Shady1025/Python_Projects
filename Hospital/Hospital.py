import sys
import datetime

from PublicFunctions.GetDBConn import ConnDB
from PublicFunctions.DateJudgement import judgeDate
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox

from HospitalUI import Ui_MainWindow
import HospVacAppointmentUI as u2
import HospWarehouseInfoUI as u3
import HospVacStorageUI as u4
import HospVacOrderUI as u5
import HospVacPurchaseUI as u6
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
        self.ui.pushButton.clicked.connect(self.UpdateVaccinationInfo)

    def UpdateVaccinationInfo(self):
        # ??????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # TODO:??????????????????HospitalNo
        HospitalNo = self.ui.lineEdit.text()
        GetVaccinationInfoSql = "SELECT * FROM `VaccinationInfo` WHERE HospitalNo = %s"
        cursor.execute(GetVaccinationInfoSql, HospitalNo)
        VaccinationInfoData = cursor.fetchall()
        if VaccinationInfoData:
            print(VaccinationInfoData)
            # TODO:????????????????????????
            InfoNo = self.ui.lineEdit_2.text()
            cursor.execute("SELECT InfoNo FROM `VaccinationInfo` WHERE HospitalNo = %s", HospitalNo)
            AllInfoNo = cursor.fetchall()
            print(AllInfoNo)
            InfoFlag = False
            for infono in AllInfoNo:
                if InfoNo == infono[0]:
                    InfoFlag = True
            if InfoFlag:
                Flag = self.ui.lineEdit_3.text()
                # TODO:????????????????????????
                if Flag == '?????????':
                    # TODO:?????????????????? ????????????????????????????????????????????????????????????
                    print('????????????????????????:')
                    Year = self.ui.lineEdit_4.text()
                    Month = self.ui.lineEdit_5.text()
                    Day = self.ui.lineEdit_6.text()
                    Hour = self.ui.lineEdit_7.text()
                    Minute = self.ui.lineEdit_8.text()
                    DateFlag = True
                    # ?????????????????????
                    date=Year+'-'+Month+'-'+Day
                    '''
                    if int(Month) < 0 or int(Month) > 12:
                        DateFlag = False
                    if DateFlag:
                        if int(Day) < 0 or int(Day) > mon[int(Month) - 1]:
                            DateFlag = False
                    '''
                    if judgeDate(date)==False:
                        DateFlag=False
                    if DateFlag:
                        if not (int(Hour) > 0 and int(Hour) < 24 and (int(Minute) >= 0) and (int(Minute) < 60)):
                            DateFlag = False
                    if DateFlag == False:
                        QMessageBox.information(self, '??????', '???????????????', QMessageBox.Close)
                        return

                    Vacctime = Year + '-' + Month + '-' + Day + ' ' + Hour + ':' + Minute + ':' + '00'
                    UpdateFinishSql = "UPDATE `VaccinationInfo` SET VaccinationTime = %s, FinishFlag = '?????????' WHERE " \
                                      "InfoNo=%s "
                    UpdateVaccineStatusSql = "UPDATE `Vaccine` SET Flag='?????????' WHERE VaccineNo = (SELECT VaccineNo " \
                                             "FROM `VaccinationInfo` WHERE InfoNo=%s) "
                    cursor.executemany(UpdateFinishSql, [(Vacctime, InfoNo)])
                    conn.commit()
                    cursor.execute(UpdateVaccineStatusSql, InfoNo)
                    conn.commit()
                    QMessageBox.information(self, '??????', '???????????????????????????', QMessageBox.Close)
                elif Flag == '?????????':
                    UpdateFinishSql = "DELETE FROM `VaccinationInfo` WHERE InfoNo=%s"
                    UpdateVaccineStatusSql = "UPDATE `Vaccine` SET Flag='?????????' WHERE VaccineNo = (SELECT VaccineNo " \
                                             "FROM `VaccinationInfo` WHERE InfoNo=%s) "
                    cursor.execute(UpdateVaccineStatusSql, InfoNo)
                    conn.commit()
                    cursor.execute(UpdateFinishSql, InfoNo)
                    conn.commit()
                    QMessageBox.information(self, '??????', '???????????????????????????', QMessageBox.Close)
                else:
                    # TODO:MessageBox????????????
                    QMessageBox.information(self, '??????', '???????????????', QMessageBox.Close)
                    # pass

            else:
                # TODO:MessageBox InfoNo?????????
                QMessageBox.information(self, '??????', 'InfoNo????????????', QMessageBox.Close)
                # pass
        else:
            # TODO:MessageBox ?????????????????????
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
            # pass
        #QMessageBox.information(self, '??????', '???????????????????????????', QMessageBox.Close)
        cursor.close()
        conn.close()


class ThirdWindow(QMainWindow):
    def slot1(self):
        win3.close()

    def __init__(self, parent = None):
        super(ThirdWindow, self).__init__(parent)
        self.ui = u3.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.GetWarehouseArea)

    def GetWarehouseArea(self):
        # ???????????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:??????????????????HospitalNo
        HospitalNo = self.ui.lineEdit.text()
        if HospitalNo=='':
            QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Close)
            return
        GetWarehouseAreaSql = "SELECT * FROM `WarehouseArea` WHERE HospitalNo = %s"
        cursor.execute(GetWarehouseAreaSql, HospitalNo)
        WarehouseData = cursor.fetchall()
        if WarehouseData:
            print(WarehouseData)
            x = 0
            for i in WarehouseData:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(WarehouseData[x][y])))
                    y = y + 1
                x = x + 1
            # TODO:????????????????????????????????????
        else:
            # TODO:????????????MessageBox?????????????????????
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            # pass


class FourthWindow(QMainWindow):
    def slot1(self):
        win4.close()

    def __init__(self, parent = None):
        super(FourthWindow, self).__init__(parent)
        self.ui = u4.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.GetInStorageData)

    def GetInStorageData(self):
        # ?????????????????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:??????????????????HospitalNo
        HospitalNo = self.ui.lineEdit.text()
        GetInStorageDataSql = "SELECT * FROM `InStorage` WHERE HospitalNo = %s"
        cursor.execute(GetInStorageDataSql, HospitalNo)
        InStorageData = cursor.fetchall()
        if InStorageData:
            print(InStorageData)
            # TODO:??????????????????????????????????????????
            x = 0
            for i in InStorageData:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(InStorageData[x][y])))
                    y = y + 1
                x = x + 1
        else:
            # TODO:????????????MessageBox?????????????????????
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            pass


class FifthWindow(QMainWindow):
    def slot1(self):
        win5.close()

    def __init__(self, parent = None):
        super(FifthWindow, self).__init__(parent)
        self.ui = u5.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.GetVaccineOrder)

    def GetVaccineOrder(self):
        # ?????????????????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:??????????????????HospitalNo
        HospitalNo = self.ui.lineEdit.text()
        if HospitalNo=='':
            QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Close)
            return
        GetVaccineOrderSql = "SELECT * FROM `VaccineOrder` WHERE HospitalNo = %s"
        cursor.execute(GetVaccineOrderSql, HospitalNo)
        VaccineOrder = cursor.fetchall()
        if VaccineOrder:
            print(VaccineOrder)
            # TODO:????????????????????????????????????
            x = 0
            for i in VaccineOrder:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccineOrder[x][y])))
                    y = y + 1
                x = x + 1
        else:
            # TODO:????????????MessageBox?????????????????????
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
            #pass


class SixWindow(QMainWindow):
    def slot1(self):
        win6.close()

    def __init__(self, parent = None):
        super(SixWindow, self).__init__(parent)
        self.ui = u6.Ui_MainWindow()
        self.ui.setupUi(self)
        # ??????,???????????????????????????self.ui.pushButton???????????????self.pushButton
        self.ui.pushButton.clicked.connect(self.BuyVaccine)
        self.ui.pushButton_3.clicked.connect(self.LastVaccine)

    def LastVaccine(self):
        # ????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:??????????????????HospitalNo???VaccineName
        HospitalNo = self.ui.lineEdit.text()
        VaccineName = self.ui.lineEdit_2.text()
        if HospitalNo=='' or VaccineName=='':
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
        GetVaccineAmountSql = "SELECT count(*) FROM `Vaccine` where VaccineName=%s and HospitalNo='???'"
        cursor.execute(GetVaccineAmountSql, VaccineName)
        AvaVaccineAmount = cursor.fetchall()[0][0]
        # TODO:???AvaVaccineAmount???????????????
        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(AvaVaccineAmount)))

    def BuyVaccine(self):
        # ????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:??????????????????HospitalNo???VaccineName
        HospitalNo = self.ui.lineEdit.text()
        VaccineName = self.ui.lineEdit_2.text()
        cursor.execute("SELECT HospitalNo FROM `Hospital`")
        AllHospitalNo=cursor.fetchall()
        #print(AllHospitalNo)
        #?????????????????????
        if HospitalNo=='' or VaccineName=='':
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
        if (HospitalNo,) not in AllHospitalNo:
            QMessageBox.information(self, '??????', '??????ID??????', QMessageBox.Close)
            return

        GetVaccineAmountSql = "SELECT count(*) FROM `Vaccine` where VaccineName=%s and HospitalNo='???'"
        cursor.execute(GetVaccineAmountSql, VaccineName)
        AvaVaccineAmount = cursor.fetchall()[0][0]
        # TODO:???AvaVaccineAmount???????????????
        # self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccineOrder[x][y])))
        print('????????????:' + str(AvaVaccineAmount))
        OrderAmount=self.ui.lineEdit_3.text()
        if OrderAmount=='':
            QMessageBox.information(self, '??????', '??????????????????', QMessageBox.Close)
            return
        OrderAmount = int(self.ui.lineEdit_3.text())

        if OrderAmount > int(AvaVaccineAmount):
            # TODO:????????????MessageBox??????????????????????????????
            print('????????????????????????!')
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
        else:
            # ??????InStorage???
            GetWarehouseSql = "SELECT WarehouseNo FROM `WarehouseArea` WHERE VaccineName = %s"
            cursor.execute(GetWarehouseSql, VaccineName)
            WarehouseNo = cursor.fetchall()[0][0]
            InStorageSql = "INSERT INTO InStorage VALUES(%s,%s,%s,%s)"
            cursor.executemany(InStorageSql, [
                (HospitalNo, WarehouseNo, OrderAmount, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))])
            conn.commit()
            # ??????Vaccine???
            cursor.execute(
                "SELECT VaccineNo FROM `Vaccine` WHERE VaccineName=%s and HospitalNo='???' ORDER BY VaccineNo asc LIMIT 1",
                VaccineName)
            NowVaccineNo = cursor.fetchall()[0][0]  # ???????????????????????????
            VaccineNotmp = NowVaccineNo[0:7]
            VaccineNumber = NowVaccineNo[7:]
            UpdateVaccineSql = "UPDATE `Vaccine` SET HospitalNo = %s, Flag='?????????', CountFlag=1 WHERE VaccineNo=%s"
            # print(NowVaccineNo)
            for i in range(int(VaccineNumber), int(VaccineNumber) + OrderAmount):
                if i < 10:
                    NextVaccineNo = VaccineNotmp + '00' + str(i)
                elif i < 100:
                    NextVaccineNo = VaccineNotmp + '0' + str(i)
                else:
                    NextVaccineNo = VaccineNotmp + str(i)
                cursor.executemany(UpdateVaccineSql, [(HospitalNo, NextVaccineNo)])
                conn.commit()
            # ??????VaccineOrder???
            GetAllProducerNoSql = "SELECT DISTINCT ProducerNo FROM `Vaccine` WHERE VaccineName=%s AND HospitalNo=%s AND CountFlag=1"
            GetProducerAmountSql = "SELECT COUNT(ProducerNo) FROM `Vaccine` WHERE VaccineName=%s AND HospitalNo=%s AND ProducerNo=%s AND CountFlag=1"
            UpdateVaccineOrderSql = "INSERT INTO `VaccineOrder` VALUES(%s,%s,%s,%s,%s)"
            cursor.executemany(GetAllProducerNoSql, [(VaccineName, HospitalNo)])
            AllProducerNo = cursor.fetchall()
            print(AllProducerNo)
            for pno in AllProducerNo:
                ProducerNo = pno[0]
                print(ProducerNo)
                cursor.executemany(GetProducerAmountSql, [(VaccineName, HospitalNo, ProducerNo)])
                InStorageAmount = cursor.fetchall()[0][0]
                print(InStorageAmount)
                cursor.executemany(UpdateVaccineOrderSql, [(HospitalNo, ProducerNo, VaccineName, InStorageAmount,
                                                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))])
                conn.commit()
            # ???????????????????????????2 ?????????????????????
            UpdateVaccineCountStatus = "UPDATE `Vaccine` SET CountFlag=2 WHERE VaccineNo=%s"
            for i in range(int(VaccineNumber), int(VaccineNumber) + OrderAmount):
                if i < 10:
                    NextVaccineNo = VaccineNotmp + '00' + str(i)
                elif i < 100:
                    NextVaccineNo = VaccineNotmp + '0' + str(i)
                else:
                    NextVaccineNo = VaccineNotmp + str(i)
                cursor.execute(UpdateVaccineCountStatus, NextVaccineNo)
                conn.commit()
            QMessageBox.information(self, '??????', '????????????', QMessageBox.Close)
        cursor.close()
        conn.close()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def slot1(self):
        win2.show()

    def slot2(self):
        win3.show()

    def slot3(self):
        win4.show()

    def slot4(self):
        win5.show()

    def slot5(self):
        win6.show()

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        # ??????????????????
        self.pushButton.clicked.connect(self.GetVaccinationInfo)

    def GetVaccinationInfo(self):
        # ??????????????????????????????????????????
        conn = ConnDB()
        cursor = conn.cursor()
        # TODO:????????????HospitalNo
        HospitalNo = self.lineEdit.text()

        GetVaccinationInfoSql = "SELECT * FROM `VaccinationInfo` WHERE HospitalNo = %s"
        cursor.execute(GetVaccinationInfoSql, HospitalNo)
        VaccinationInfoData = cursor.fetchall()
        if VaccinationInfoData:
            # TODO:????????????????????????
            print(VaccinationInfoData)
            x = 0
            for i in VaccinationInfoData:
                y = 0
                for j in i:
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccinationInfoData[x][y])))
                    y = y + 1
                x = x + 1
        else:
            # TODO:????????????MessageBox??????
            QMessageBox.information(self, '??????', '?????????????????????????????????', QMessageBox.Close)
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
    win5 = FifthWindow()
    win6 = SixWindow()
    sys.exit(app.exec())
