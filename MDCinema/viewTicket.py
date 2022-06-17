# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'ViewTicket.ui'
#
# Created by: PyQt5 UI code generator 5.15.4



from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class view_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_MAID = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_MAID.setFont(font)
        self.lineEdit_MAID.setObjectName("lineEdit_MAID")
        self.horizontalLayout.addWidget(self.lineEdit_MAID)
        self.pushButton_viewTicket = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_viewTicket.setFont(font)
        self.pushButton_viewTicket.setObjectName("pushButton_viewTicket")
        self.pushButton_viewTicket.clicked.connect(self.viewTicket)
        self.horizontalLayout.addWidget(self.pushButton_viewTicket)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_moviename = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_moviename.setFont(font)
        self.label_moviename.setObjectName("label_moviename")
        self.verticalLayout.addWidget(self.label_moviename)
        self.label_startTime = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_startTime.setFont(font)
        self.label_startTime.setObjectName("label_startTime")
        self.verticalLayout.addWidget(self.label_startTime)
        self.label_Endtime = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Endtime.setFont(font)
        self.label_Endtime.setObjectName("label_Endtime")
        self.verticalLayout.addWidget(self.label_Endtime)
        self.label_ScreenHall = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ScreenHall.setFont(font)
        self.label_ScreenHall.setObjectName("label_ScreenHall")
        self.verticalLayout.addWidget(self.label_ScreenHall)
        self.label_warning = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning.setFont(font)
        self.label_warning.setObjectName("label_warning")
        self.verticalLayout.addWidget(self.label_warning)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    # 检测输入的MAID 是否在MocieMenu 中。
    # 
    def ticketIsMAID(self,MAID):
        flag  = None
        try :
            conn  = sqlite3.connect("cinema.db")
            cur = conn.cursor()
            sql = "SELECT ID FROM MovieArrangement WHERE ID = {}".format(MAID)
            cur.execute(sql)
            flag = cur.fetchone()
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        return flag

    def viewTicket(self):
        MAID = self.lineEdit_MAID.text()
        flag = self.ticketIsMAID(MAID)
        if flag!= None:
            try:
                conn = sqlite3.connect("cinema.db")
                cur = conn.cursor()
                sql ='''
                SELECT 
                M.MovieName,MA.StartTime,MA.EndTime,MA.HallID
                FROM 
                Movie M,MovieArrangement MA
                WHERE 
                M.MovieID=MA.MovieID and MA.ID = {}'''.format(MAID)
                cur.execute(sql)
                result= cur.fetchone()
                self.label_moviename.setText("Movie Name: "+result[0])
                self.label_startTime.setText("Starttime: "+ result[1])
                self.label_Endtime.setText("EndTime: "+ result[2])
                self.label_ScreenHall.setText("ScreenHall No. "+ str(result[3]))
                self.label_warning.setText("Enjoy your movie!!!!")
                conn.commit()
            except sqlite3.Error as e :
                print(e)
        else:
            self.label_warning.setText("Warning : Please Enter Right MAID!")
            self.label_moviename.setText("")
            self.label_startTime.setText("")
            self.label_Endtime.setText("")
            self.label_ScreenHall.setText("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Ticket"))
        self.lineEdit_MAID.setPlaceholderText(_translate("Dialog", "Please Enter the MAID"))
        self.pushButton_viewTicket.setText(_translate("Dialog", "View Ticket"))
        self.label_moviename.setText(_translate("Dialog", "Movie Name:"))
        self.label_startTime.setText(_translate("Dialog", "Starttime:"))
        self.label_Endtime.setText(_translate("Dialog", "EndTime:"))
        self.label_ScreenHall.setText(_translate("Dialog", "ScreenHall"))
        self.label_warning.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
