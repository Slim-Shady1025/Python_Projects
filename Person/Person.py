import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PublicFunctions.GetDBConn import ConnDB
from PublicFunctions.DateJudgement import judgeDate
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox

from PersonInfo import Ui_MainWindow
import SearchInfo as u2
import MakeAppointment as u3
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
        
        if len(PasswordText) < 6:
            QMessageBox.information(None, 'Error', '        ?????????????????????     ')
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
        self.ui.pushButton.clicked.connect(self.SearchVaccinationinfo)

    def SearchVaccinationinfo(self):
        # ??????:self ????????????????????????????????? def SearchVaccinationinfo(self)
        # ??????: ??????????????????True ???????????????False
        # ????????????????????????
        # TODO:????????????????????????ID
        PersonID = self.ui.lineEdit.text()
        conn = ConnDB()
        cursor = conn.cursor()
        sql = 'SELECT * FROM `VaccinationInfo` where PersonID = %s'
        cursor.execute(sql, PersonID)

        VaccinationInfoData = cursor.fetchall()
        if VaccinationInfoData:
            x = 0
            for i in VaccinationInfoData:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(VaccinationInfoData[x][y])))
                    y = y + 1
                x = x + 1
            print(VaccinationInfoData)
            cursor.close()
            return True
        else:
            # TODO:????????????MessageBox?????????????????????
            QMessageBox.information(self, '??????', '???????????????', QMessageBox.Close)


class ThirdWindow(QMainWindow):
    def slot2(self):
        win3.close()

    def __init__(self, parent = None):
        super(ThirdWindow, self).__init__(parent)
        self.ui = u3.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.SearchHospital)
        self.ui.pushButton_4.clicked.connect(self.SubmitNewVaccinationInfo)

    def SearchHospital(self):
        # ??????:self
        # ??????: ????????????????????????????????????True ????????????False
        # ??????????????????????????????
        # TODO:???????????????????????????
        PersonID = self.ui.lineEdit.text()
        VaccineName = self.ui.lineEdit_2.text()
        if PersonID=='':
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
            return
        if VaccineName=='':
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
            return
        conn = ConnDB()
        cursor = conn.cursor()
        FindHospitalSql = "SELECT DISTINCT Hospital.HospitalNo,Hospital.HospitalName FROM `Hospital` LEFT JOIN " \
                          "`Vaccine` ON Hospital.HospitalNo=Vaccine.HospitalNo WHERE Vaccine.VaccineName = %s AND " \
                          "Vaccine.Flag='?????????' "
        cursor.execute(FindHospitalSql, VaccineName)
        AvaHospital = cursor.fetchall()
        # TODO:????????????ID???????????????????????????????????????????????????/???????????????????????????
        if AvaHospital:
            # TODO:???????????????????????????????????????????????????
            x = 0
            for i in AvaHospital:
                y = 0
                for j in i:
                    self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(AvaHospital[x][y])))
                    y = y + 1
                x = x + 1
            print(AvaHospital)
        else:
            # TODO:????????????MessageBox??????????????????????????????
            QMessageBox.information(self, '??????', '????????????????????????????????????', QMessageBox.Close)
            #pass

    def SubmitNewVaccinationInfo(self):
        # ??????:self
        # ??????: ????????????????????????????????????True ????????????False
        # ??????????????????????????????
        # TODO:???????????????????????????

        VaccineName = self.ui.lineEdit_2.text()
        PersonID = self.ui.lineEdit.text()
        HospitalNo = self.ui.lineEdit_3.text()
        Date = self.ui.lineEdit_4.text()
        #????????????????????????????????????
        if PersonID=='':
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
            return
        if VaccineName=='':
            QMessageBox.information(self, '??????', '????????????????????????', QMessageBox.Close)
            return

        conn = ConnDB()
        cursor = conn.cursor()
        FindHospitalSql = "SELECT DISTINCT Hospital.HospitalNo,Hospital.HospitalName FROM `Hospital` LEFT JOIN " \
                          "`Vaccine` ON Hospital.HospitalNo=Vaccine.HospitalNo WHERE Vaccine.VaccineName = %s AND " \
                          "Vaccine.Flag='?????????' "
        cursor.execute(FindHospitalSql, VaccineName)
        AvaHospital = cursor.fetchall()
        if AvaHospital:
            # TODO:????????????ID???????????????????????????????????????????????????/???????????????????????????
            Flag = False
            for hospital in AvaHospital:
                print(hospital[0])
                if HospitalNo == hospital[0]:
                    Flag = True
            if not Flag:
                # TODO:????????????MessageBox???????????????????????????
                QMessageBox.information(self, '??????', '???????????????????????????', QMessageBox.Close)
                return

            GetVaccineNoSql = "SELECT VaccineNo FROM `Vaccine` WHERE HospitalNo=%s AND Flag='?????????' AND VaccineName=%s order by VaccineNo asc " \
                              "limit 1 "
            cursor.executemany(GetVaccineNoSql, [(HospitalNo,VaccineName)])
            VaccineNo = cursor.fetchall()[0][0]
            print(VaccineNo)
            #Date = self.ui.lineEdit_4.text()
            #VaccineName = self.ui.lineEdit_2.text()
            InfoIDSql = "SELECT InfoNo FROM `VaccinationInfo` order by InfoNo desc limit 1"
            BatchIDSql = "SELECT Batch FROM `VaccinationInfo` LEFT JOIN `Vaccine` ON " \
                         "VaccinationInfo.VaccineNo=Vaccine.VaccineNo WHERE PersonID=%s AND Vaccine.VaccineName=%s order " \
                         "by Batch desc limit 1 "
            cursor.execute(InfoIDSql)
            InfoID = cursor.fetchall()[0][0]
            InfoIDNumber = int(InfoID[6:]) + 1
            if InfoIDNumber < 10:
                InfoID = InfoID[0:6] + '000' + str(InfoIDNumber)
            elif InfoIDNumber < 100:
                InfoID = InfoID[0:6] + '00' + str(InfoIDNumber)
            elif InfoIDNumber < 1000:
                InfoID = InfoID[0:6] + '0' + str(InfoIDNumber)
            else:
                InfoID = InfoID[0:6] + str(InfoIDNumber)
            print(InfoID)
            cursor.executemany(BatchIDSql, [(PersonID, VaccineName)])
            Batch = cursor.fetchall()
            if Batch:
                Batch = int(Batch[0][0]) + 1
            else:
                Batch = 1
            print(Batch)
            if judgeDate(Date):
                VaccinationInfoSql = "INSERT INTO `VaccinationInfo` VALUES (%s,%s,%s,%s,%s,%s,NULL,'?????????')"
                cursor.executemany(VaccinationInfoSql, [(InfoID, PersonID, HospitalNo, VaccineNo, Batch, Date)])
                conn.commit()
                UpdateVaccineStatus = "UPDATE `Vaccine` SET Flag='?????????' WHERE VaccineNo = %s"
                QMessageBox.information(self, '????????????', '?????????????????????????????????????????????????????????', QMessageBox.Close)
                cursor.execute(UpdateVaccineStatus, VaccineNo)
            else:
                QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Close)
            conn.commit()
            conn.close()
        else:
            QMessageBox.information(self, '??????', '?????????????????????????????????', QMessageBox.Close)
            return

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def slot1(self):
        win2.show()

    def slot2(self):
        win3.show()

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        # ??????????????????
        self.pushButton.clicked.connect(self.SearchPersonInfo)

    def SearchPersonInfo(self):
        PersonID = self.lineEdit.text()
        print(PersonID)
        conn = ConnDB()
        cur = conn.cursor()

        # ?????????sql??????
        sql = "SELECT * FROM Person WHERE PersonID=%s"
        cur.execute(sql, PersonID)
        data = cur.fetchall()

        # ????????????
        print(data)
        if data:
            x = 0
            for i in data:
                y = 0
                for j in i:
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                    y = y + 1
                x = x + 1
        else:
            QMessageBox.information(self, '??????', '???????????????????????????,??????????????????ID', QMessageBox.Close)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win0 = StartDesinger()
    win0.show()
    win = MyMainWindow()
    win2 = SecondWindow()
    win3 = ThirdWindow()
    sys.exit(app.exec())
